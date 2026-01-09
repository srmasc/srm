# Certificate Generator Website 🎓

A simple and elegant PHP-based certificate generator that allows you to create beautiful certificates in seconds.

## Features

- ✨ Clean and intuitive user interface
- 📝 Customizable certificate fields (recipient name, course, issuer, date, description)
- 🎨 Beautiful certificate design with gradient borders
- 🏆 Multiple certificate types (Achievement, Completion, Appreciation, Excellence)
- 🖨️ Print-friendly layout
- 📱 Responsive design for mobile and desktop
- 🔒 Secure input handling with PHP sanitization

## Requirements

- PHP 7.0 or higher
- Web server (Apache, Nginx, or PHP built-in server)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/srmasc/srm.git
   cd srm
   ```

2. Start a PHP development server:
   ```bash
   php -S localhost:8000
   ```

3. Open your browser and navigate to:
   ```
   http://localhost:8000/certificate.php
   ```

## Usage

1. **Access the form**: Open `certificate.php` in your web browser
2. **Fill in the details**:
   - Enter the recipient's name (required)
   - Add the course or achievement title (required)
   - Specify who is issuing the certificate (required)
   - Select the date (defaults to today)
   - Optionally add a description
   - Choose the certificate type (Achievement, Completion, Appreciation, or Excellence)
3. **Generate**: Click the "Generate Certificate" button
4. **Print or Save**: 
   - The certificate opens in a new tab/window
   - Click "Print Certificate" to print or save as PDF
   - Click "Create Another" to generate a new certificate

## Files

- `certificate.php` - Main form page for entering certificate details
- `generate.php` - Certificate generation and display page
- `README.md` - Documentation

## How It Works

1. **certificate.php**: Displays a form where users enter certificate information
2. **generate.php**: Receives form data via POST, sanitizes it, and generates a beautifully formatted certificate
3. The certificate can be printed or saved as PDF using the browser's print function

## Security

- All user inputs are sanitized using `htmlspecialchars()` to prevent XSS attacks
- Form validation ensures required fields are filled

## Browser Compatibility

Works on all modern browsers:
- Chrome/Edge (recommended)
- Firefox
- Safari
- Opera

## Customization

You can customize the certificate design by editing the CSS in `generate.php`:
- Change colors by modifying the gradient values
- Adjust fonts in the style section
- Modify the layout and spacing

## License

This project is open source and available for personal and commercial use.