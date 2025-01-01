"""reotp - generate provisioning URIs or QR codes for OTPs.

A light wrapper around `pyotp` and `qrcode[pil]` for regenerating QR codes
for which you have the secret.  Use it to transfer existing OTPs between
services like Google Authenticator.

Invoke me using the packaged script stub `reotp` or as a Python module
`python -m reotp`.
"""
import sys
import pyotp
import qrcode
import base64
import hashlib
import pathlib
import argparse
import urllib.parse
from reotp import pbotp

DEFAULT_DIGITS = 6
ALLOWED_DIGITS = [6, 8]
DEFAULT_ALGORITHM = 'sha1'
ALLOWED_ALGORITHMS = ['sha1', 'sha256', 'sha512', 'md5']
DEFAULT_PERIOD = 30


def parse_args():
    """Parse the command line arguments."""
    parser = argparse.ArgumentParser(description="Regenerate an existing OTP.")

    qr_options = parser.add_argument_group("QR options")
    qr_options.add_argument('-i', '--issuer', type=str, required=False,
                        help=("Issuer for TOTP. "
                              "This is the name that will appear in your app.")
                        )
    qr_options.add_argument('-u', '--user', type=str, required=False,
                        default="", help=(
                            "Username for the OTP. "
                            "If not provided library defaults to 'Secret'.")
                        )

    output = parser.add_argument_group("qr output")
    output.add_argument('-a', '--qrcode-ascii', action='store_true',
                        help='Display an ascii QR code for the OTP.')
    output.add_argument('-q', '--qrcode-preview', action='store_true',
                        help='Display a QR code image for the OTP.')
    output.add_argument('-f', '--qrcode-png',
                        type=pathlib.Path, metavar="PATH",
                        help='Write the QR code image for the OTP to a file.')
    output.add_argument('-p', '--provisioning-uri', action='store_true',
                        help='Print the QR code provisioning URI.')

    subparsers = parser.add_subparsers(dest='mode')
    secret_parser = subparsers.add_parser(
            "regenerate", help="Regenerate from a known secret.")
    secret_parser.add_argument('-s', '--secret', type=str, required=False,
                        default="", help=(
                            "Secret for the TOTP. "
                            "If not provided, requested interactively "
                            "so you don't leak the secret in shell history.")
                        )

    advanced = secret_parser.add_argument_group(
            'Advanced', 'Advanced options that you probably do not need.')
    advanced.add_argument('-c', '--counter', type=int, default=-1,
                          metavar="CURRENT_COUNT",
                          help='Counter based OTP with current count.')
    advanced.add_argument('-d', '--digits', type=int,
                          choices=ALLOWED_DIGITS,
                          default=DEFAULT_DIGITS, help='Number of digits.')
    advanced.add_argument('-a', '--algorithm', type=str,
                          choices=ALLOWED_ALGORITHMS,
                          default=DEFAULT_ALGORITHM, help='Hashing algorithm.')
    advanced.add_argument('-p', '--period', type=int,
                          default=DEFAULT_PERIOD,
                          help='Refresh period in seconds.')

    migration_parser = subparsers.add_parser(
            "migration", help="Regenerate from otpauth-migration URI.")
    migration_parser.add_argument("-m", "--migration-uri", metavar="URI",
                                  required=False,
                                  help=("otpauth-migration:// URI. "
                                        "If not provided, requested "
                                        "interactively.")
                                  )
    return parser.parse_args()

def get_input(prompt="Secret: "):
    """Get the secret if it wasn't included in the script args."""
    if sys.stdin.isatty():
        secret = input(prompt)
    else:
        secret = input()
    return secret.strip()

def regenerate(secret,
               digits=DEFAULT_DIGITS,
               algorithm=hashlib.sha1,
               counter=-1,
               period=DEFAULT_PERIOD):
    otp = None
    if counter >= 0:
        # Counter based HOTPs takes initial count.
        otp = pyotp.HOTP(secret, digits=digits, digest=algorithm,
                         initial_count=counter)
    else:
        # Time based TOTPs take period/interval
        otp = pyotp.TOTP(secret, digits=digits, digest=algorithm,
                         interval=period)
    return otp

def migrate(migration_uri):
    """Convert a migration URL into an OTP object.

    The `migration_uri` should have the format:
    `otpauth-migration://offline?data=<urlencoded base64 protobuf>`
    """
    # Break the URI into components, parse the query string, extract data.
    migration_uri_components  = urllib.parse.urlparse(migration_uri)
    migration_data = urllib.parse.parse_qs(
            migration_uri_components.query)['data'][0]
    # Data may need padding with `=`, Authenticator implementation may not pad.
    migration_data += '=' * (len(migration_uri) % 4)

    # Create an instance or our protobuf structure and populate it.
    mp = pbotp.MigrationPayload()
    mp.ParseFromString(base64.b64decode(migration_data))

    # Extract the OTP params for the only migration uri in there
    # (we only extract one).
    otp_params = mp.otp_parameters[0]

    # The secret is just a byte string and needs base32 encoding for the app.
    secret = base64.b32encode(otp_params.secret).decode()

    # Map values between protobuf enum and real values pyotp requires.
    digits = DEFAULT_DIGITS
    algorithm = hashlib.sha1
    if otp_params.digits != mp.DIGIT_COUNT_SIX:
        digits = 8

    if otp_params.algorithm == mp.ALGORITHM_SHA256:
        algorithm = hashlib.sha256
    elif otp_params.algorithm == mp.ALGORITHM_SHA512:
        algorithm = hashlib.sha512
    elif otp_params.algorithm == mp.ALGORITHM_MD5:
        algorithm = hashlib.md5

    # Create the OTP object.
    if otp_params.type == mp.OTP_TYPE_TOTP:
        otp = pyotp.TOTP(secret,
                         digits=digits,
                         digest=algorithm,
                         interval=DEFAULT_PERIOD)
    elif otp_params.type == mp.OTP_TYPE_HOTP:
        otp = pyotp.HOTP(secret, digits=digits, digest=algorithm,
                         initial_count=otp_params.counter)
    else:
        raise ValueError("Unknown OTP type - not TOTP or HOPT.")

    # Return the OTP and any issuer or name info extracted,
    # in case the user didn't provide them for the QR.
    return (otp, otp_params.issuer, otp_params.name)


def main():
    args = parse_args()

    # When creating the QR, we can pass an issuer and name.
    # Use the command line args even if they come in the
    # migration data.
    uri_args = {
            'issuer_name': args.issuer,
            'name': args.user
            }

    if args.mode == 'regenerate':
        # The secret is provided either as argument or on stdin.
        secret = args.secret
        if not secret:
            secret = get_input()

        # pyotp expects the hashlib digest, make sure it exists.
        algorithm = hashlib.sha1
        if args.algorithm:
            if hasattr(hashlib, args.algorithm):
                algorithm = getattr(hashlib, args.algorithm)
            else:
                raise ValueError(f"{args.algorithm} not supported by hashlib!")
                sys.exit(1)

        try:
            # generate an OTP object with the attributes provided.
            otp = regenerate(secret, digits=args.digits, algorithm=algorithm,
                             period=args.period, counter=args.counter)
        except ValueError as e:
            # ValueErrors are raised when the input data violates the spec.
            # see https://pyauth.github.io/pyotp/
            print(f"Failed to generate OTP, bad values provided: {e}.")
            sys.exit(1)


    elif args.mode == 'migration':
        # Migration URI can also come from either args or stdin.
        migration_uri = args.migration_uri
        if not migration_uri:
            migration_uri = get_input('Migration URI: ')

        # Generate a new OTP object based on the migration schema.
        try:
            otp, issuer, name = migrate(migration_uri)
        except ValueError as e:
            print(f"Failed to migrate OTP, bad values in URI: {e}.")
            sys.exit(1)

        # If the issuer or name were not provided as args, use the
        # values from the migration data.
        if not uri_args['issuer_name']:
            uri_args['issuer_name'] = issuer
        if not uri_args['name']:
            uri_args['name'] = name

    # Generate the provisioning URI for this TOTP with issuer and name.
    uri = otp.provisioning_uri(**uri_args)

    if args.provisioning_uri:
        print(uri)

    # Create a QR Code object, and print it to console if asked.
    qr = qrcode.QRCode()
    qr.add_data(uri)
    if args.qrcode_ascii:
        qr.print_ascii()

    # Create an image object for the QR, and display or write it.
    if args.qrcode_preview or args.qrcode_png:
        qr_img = qr.make_image()

        if args.qrcode_preview:
            qr_img.show()
        if args.qrcode_png:
            try:
                qr_img.save(args.qrcode_png)
            except IOError as e:
                print(f"Failed to write QR code to file: {e}")
                sys.exit(2)

# Entrypoint for shim and module execution.
if __name__ == '__main__':
    main()
