# reotp

This project is a **One Time Passcode (OTP) Regenerator** that you can use
to regenerate OTP provisioning URIs and QR codes.  Useful for transitioning
existing OTPs to a new service or app, like Google Authenticator.

## Features

- Create and display or save QR codes for your existing OTPs.
- Support for both Time (TOTP) and Counter (HOTP) based OTPs.
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

The python package installs a shim, so you can run it from the command line:

```
$ reotp --help
usage: reotp [-h] -i ISSUER [-s SECRET] [-u USER] [-q] [-f PATH] [-c CURRENT_COUNT]
             [-d DIGITS] [-a ALGORITHM] [-p PERIOD]

Regenerate an existing OTP.

options:
  -h, --help            show this help message and exit
  -i ISSUER, --issuer ISSUER
                        Issuer for TOTP. This is the name that will appear in your app.
  -s SECRET, --secret SECRET
                        Secret for the TOTP. If not provided, requested interactively so
                        you don't leak the secret in shell history.
  -u USER, --user USER  Username for the OTP. If not provided library defaults to
                        'Secret'.
  -q, --qrcode          Display a QR code for the OTP.
  -f PATH, --qrcode-png PATH
                        Write the QR code for the OTP to a file.

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
```


```bash
reotp -i YourIssuer -s YourSecret -u YourUsername -q -f path/to/your/qr_code.png
```

### Command Line Arguments

- `-i` or `--issuer`: (Required) Issuer for the TOTP.
- `-s` or `--secret`: (Optional) Secret for the TOTP.
- `-u` or `--user`: (Optional) Username for the service.
- `-q` or `--qrcode`: (Optional) Display a QR code for the TOTP.
- `-f` or `--qrcode-png`: (Optional) Write the QR code to a specified file.
- Advanced options (Optional):
  - `-d` or `--digits`: Number of digits for this OTP.
  - `-c` or `--counter`: Counter-based OTP.
  - `-a` or `--algorithm`: Hashing algorithm.
  - `-p` or `--period`: Refresh period.

## Examples

To generate a TOTP provisioning URI and display a QR code, you would run:

```bash
reotp -i ExampleIssuer -s JBSWY3DPEHPK3PXP -u exampleuser -q
```

To generate an HOTP (counter based) with a current count of 100, using sha256
and a length of seven:

```bash 
reotp -i MyIssuer -s JBSWY3DPEHPK3PXP -q -a sha256 -l 7 -c 100
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
