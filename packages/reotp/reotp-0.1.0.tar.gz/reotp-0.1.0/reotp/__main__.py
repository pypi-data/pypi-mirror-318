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
import hashlib
import pathlib
import argparse

DEFAULT_DIGITS = 6
DEFAULT_ALGORITHM = 'sha1'
DEFAULT_PERIOD = 30

def parse_args():
    """Parse the command line arguments."""
    parser = argparse.ArgumentParser(description="Regenerate an existing OTP.")
    parser.add_argument('-i', '--issuer', type=str, required=True,
                        help=("Issuer for TOTP. "
                              "This is the name that will appear in your app.")
                        )
    parser.add_argument('-s', '--secret', type=str, required=False,
                        default="", help=(
                            "Secret for the TOTP. "
                            "If not provided, requested interactively "
                            "so you don't leak the secret in shell history.")
                        )
    parser.add_argument('-u', '--user', type=str, required=False,
                        default="", help=(
                            "Username for the OTP. "
                            "If not provided library defaults to 'Secret'.")
                        )
    parser.add_argument('-q', '--qrcode', action='store_true',
                        help='Display a QR code for the OTP.')
    parser.add_argument('-f', '--qrcode-png',
                        type=pathlib.Path, metavar="PATH",
                        help='Write the QR code for the OTP to a file.')

    advanced = parser.add_argument_group(
            'Advanced', 'Advanced options that you probably do not need.')
    advanced.add_argument('-c', '--counter', type=int, default=-1,
                          metavar="CURRENT_COUNT",
                          help='Counter based OTP with current count.')
    advanced.add_argument('-d', '--digits', type=int, choices=[6, 8],
                          default=DEFAULT_DIGITS, help='Number of digits.')
    advanced.add_argument('-a', '--algorithm', type=str,
                          default=DEFAULT_ALGORITHM, help='Hashing algorithm.')
    advanced.add_argument('-p', '--period', type=int,
                          default=DEFAULT_PERIOD,
                          help='Refresh period in seconds.')

    return parser.parse_args()

def get_secret():
    """Get the secret if it wasn't included in the script args."""
    secret = input("Secret: ")
    return secret.strip().upper()

def main():
    """Regenerate the URI and the QR code if requested."""
    args = parse_args()

    secret = args.secret
    if not secret:
        secret = get_secret()

    # Only the issuer name is required to generate the URI.
    uri_args = {
            'issuer_name': args.issuer,
            }

    # Optional arguments should be ommitted so the library defaults are used.
    if args.user:
        uri_args['name'] = args.user

    algorithm = hashlib.sha1
    if args.algorithm:
        if hasattr(hashlib, args.algorithm):
            algorithm = getattr(hashlib, args.algorithm)
        else:
            raise ValueError(f"{args.algorithm} not supported by hashlib!")
            sys.exit(1)

    try:
        otp = None
        if args.counter >= 0:
            # Counter based HOTPs support only name, and initial count.
            otp = pyotp.HOTP(secret, digits=args.digits, digest=algorithm,
                             initial_count=args.counter)
        else:
            # Time based TOTP support algorithm and period
            otp = pyotp.TOTP(secret, digits=args.digits, digest=algorithm,
                             interval=args.period)
    except ValueError as e:
        # ValueErrors are raised when the input data violates the spec.
        # see https://pyauth.github.io/pyotp/
        print(f"Failed to generate OTP, bad values provided: {e}.")
        sys.exit(1)

    uri = otp.provisioning_uri(**uri_args)
    print(uri)

    if args.qrcode or args.qrcode_png:
        qr = qrcode.make(uri)
        if args.qrcode:
            qr.show()
        if args.qrcode_png:
            try:
                qr.save(args.qrcode_png)
            except IOError as e:
                print(f"Failed to write QR code to file: {e}")
                sys.exit(2)

if __name__ == '__main__':
    main()
