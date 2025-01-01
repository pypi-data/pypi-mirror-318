# reotp

This project is a **One Time Passcode (OTP) Regenerator** that you can use
to regenerate OTP provisioning URIs and QR codes, or to parse Google 
Authenticator exports.  Useful for transitioning
existing OTPs to a new service or app, like Google Authenticator.

I had a problem: I wanted to migrate my Google OTP, for which I only had the
Authenticator export, to another application (migration).  I also wanted to add 
an OTP to Authenticator for which I only had the secret (regeneration). 
This utility lets me do both!

## Features

- Create and display or save QR codes for your existing OTPs.
- Support for both Time (TOTP) and Counter (HOTP) based OTPs.
- Generate new provisioning OTPs from Google Authenticator exports.
- Advanced parameters for OTPs that use non-standard algothms, length, 
  or periods.

## Installation

Install using pip, or your preferred python package manager, from pypi:

```
pip install reotp
```

If you want to download and tinker, just clone or fork the repo:

```
git clone https://github.com/cbinckly/reotp.git
```

## Usage

The python package installs a shim, `reotp`, so you can run it from the command line.  
It has two modes of operation: `regenerate` to create a provisioning QR Code
from a secret; `migration` to create one for an `otpauth-migration` URI.

Although you can provide secrets and URIs as arguments, better to
provide them interactively so they aren't saved in your shell history.

```
$ reotp --help
usage: reotp [-h] [-i ISSUER] [-u USER] [-a] [-q] [-f PATH] [-p] {regenerate,migration} ...

Regenerate an existing OTP.

positional arguments:
  {regenerate,migration}
    regenerate          Regenerate from secret.
    migration           Regenerate from otpauth-migration URI.

options:
  -h, --help            show this help message and exit

QR Options:
  -i ISSUER, --issuer ISSUER
                        Issuer for TOTP. This is the name that will appear in your app.
  -u USER, --user USER  Username for the OTP. If not provided library defaults to 'Secret'.

Output Options:
  -a, --qrcode-ascii    Display an ascii QR code for the OTP.
  -q, --qrcode-preview  Display a QR code image for the OTP.
  -f PATH, --qrcode-png PATH
                        Write the QR code image for the OTP to a file.
  -p, --provisioning-uri
                        Print the QR code provisioning URI.
---

$ reotp regenerate --help
usage: reotp regenerate [-h] [-s SECRET] [-c CURRENT_COUNT] [-d {6,8}] [-a ALGORITHM] [-p PERIOD]

options:
  -h, --help            show this help message and exit
  -s SECRET, --secret SECRET
                        Secret for the TOTP. If not provided, requested interactively so you don't leak the secret in shell history.

Advanced:
  Advanced options that you probably do not need.

  -c CURRENT_COUNT, --counter CURRENT_COUNT
                        Counter based OTP with current count.
  -d {6,8}, --digits {6,8}
                        Number of digits.
  -a ALGORITHM, --algorithm ALGORITHM
                        Hashing algorithm.
  -p PERIOD, --period PERIOD
                        Refresh period in seconds.
---

$ reotp migration --help
usage: reotp migration [-h] [-m URI]

options:
  -h, --help            show this help message and exit
  -m URI, --migration-uri URI
                        otpauth-migration:// URI. If not provided, requested interactively.
```

Use the regenerate function to create a new provisioning URI:

```bash
reotp -i YourIssuer -u YourUsername -q -f path/to/your/qr_code.png regenerate -s YourSecret 
```

Use the migration function to create a new provisioning URI from a migration URI:

```bash
reotp -i YourIssuer -u YourUsername -q -f path/to/your/qr_code.png migration -m otpauth+migration://offline?...
```

## Examples

To generate a TOTP provisioning URI from a secret and display a QR code, you would run:

```bash
$ reotp -i ExampleIssuer -u exampleuser -q regenerate -s MYSUPERSECRET123
```

Or, even better, provide the secret interactively:

```bash
$ reotp -i ExampleIssuer -u exampleuser -q regenerate
Secret: MYSUPERSECRET123
```

To generate an HOTP (counter based) with a current count of 100, using sha256
and a length of seven:

```bash 
$ reotp -i MyIssuer -q regenerate -a sha256 -d 7 -c 100
Secret: MYSUPERSECRET123
```

To migrate a Google Authenticator export to a new provisioning URL:

```bash 
$ reotp -i MyIssuer -u MyUserName -q migrate 
Migration URI: otpauth-migration://offline?data=...
```

You can use the zbar binaries, like zbarimg or zbarcam, to pipe the 
migration URI directly. Given an exported QR code in 
`exported_google_otp_qr.png` that we want a new provisioning QR Code
for:

```bash
$ zbarimg -q --raw exported_google_otp_qr.png | reotp -q migrate
```

If you're constrained to working at a shell, no problem, print the
QR Code as ascii to the console!

```bash
$ zbarimg -q --raw exported_google_otp_qr.png | reotp -a migrate
```

## Contributing

Contributions are welcome! If you have suggestions for improvements, feel free to fork the repository, make your changes, and submit a pull request.

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature and more details regarding the change'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

The protobuf schema for OTP migration is from 
https://alexbakker.me/post/parsing-google-auth-export-qr-code.html
and licensed under CC-SA-BY 4.0. Thanks Alex!
