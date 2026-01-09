<?php
// Get form data
$recipientName = htmlspecialchars($_POST['recipientName'] ?? '');
$courseName = htmlspecialchars($_POST['courseName'] ?? '');
$issuerName = htmlspecialchars($_POST['issuerName'] ?? '');
$date = htmlspecialchars($_POST['date'] ?? '');
$description = htmlspecialchars($_POST['description'] ?? '');
$certificateType = htmlspecialchars($_POST['certificateType'] ?? 'achievement');

// Format date
$dateObj = DateTime::createFromFormat('Y-m-d', $date);
$formattedDate = $dateObj ? $dateObj->format('F j, Y') : date('F j, Y');

// Certificate type titles
$certificateTitles = [
    'achievement' => 'Certificate of Achievement',
    'completion' => 'Certificate of Completion',
    'appreciation' => 'Certificate of Appreciation',
    'excellence' => 'Certificate of Excellence'
];

$certificateTitle = $certificateTitles[$certificateType] ?? 'Certificate of Achievement';
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Certificate - <?php echo $recipientName; ?></title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Georgia', serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }

        .certificate-container {
            background: white;
            max-width: 1000px;
            margin: 20px auto;
            box-shadow: 0 15px 40px rgba(0,0,0,0.3);
            border-radius: 10px;
            overflow: hidden;
        }

        .certificate {
            background: linear-gradient(to bottom, #ffffff 0%, #f8f9ff 100%);
            padding: 60px;
            position: relative;
        }

        .certificate-border {
            border: 15px solid transparent;
            border-image: linear-gradient(135deg, #667eea, #764ba2) 1;
            padding: 40px;
        }

        .certificate-header {
            text-align: center;
            margin-bottom: 40px;
            border-bottom: 3px solid #667eea;
            padding-bottom: 20px;
        }

        .certificate-title {
            font-size: 2.8rem;
            color: #667eea;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 4px;
            margin-bottom: 10px;
        }

        .certificate-body {
            text-align: center;
            margin: 50px 0;
        }

        .certificate-text {
            font-size: 1.3rem;
            color: #666;
            margin: 20px 0;
            font-style: italic;
        }

        .recipient-name {
            font-size: 3rem;
            color: #333;
            margin: 30px 0;
            font-weight: 700;
            border-bottom: 3px solid #333;
            display: inline-block;
            padding: 15px 40px;
            font-family: 'Brush Script MT', cursive, 'Georgia', serif;
        }

        .course-name {
            font-size: 2rem;
            color: #764ba2;
            margin: 30px 0;
            font-weight: 600;
        }

        .certificate-description {
            font-size: 1.2rem;
            color: #666;
            margin: 30px auto;
            max-width: 700px;
            line-height: 1.8;
        }

        .certificate-footer {
            display: flex;
            justify-content: space-around;
            align-items: flex-end;
            margin-top: 80px;
            padding-top: 40px;
        }

        .signature-section {
            flex: 1;
            text-align: center;
        }

        .signature-line {
            width: 250px;
            height: 2px;
            background: #333;
            margin: 0 auto 15px;
        }

        .issuer-name {
            font-size: 1.3rem;
            font-weight: 600;
            color: #333;
            margin-bottom: 8px;
        }

        .issuer-title {
            font-size: 1rem;
            color: #666;
            font-style: italic;
        }

        .date-section {
            flex: 1;
            text-align: center;
        }

        .date-label {
            font-size: 1rem;
            color: #666;
            margin-bottom: 8px;
            font-style: italic;
        }

        .certificate-date {
            font-size: 1.2rem;
            font-weight: 600;
            color: #333;
        }

        .decorative-element {
            width: 100px;
            height: 100px;
            margin: 0 auto 20px;
        }

        .decorative-element svg {
            width: 100%;
            height: 100%;
            fill: #667eea;
        }

        .action-buttons {
            text-align: center;
            padding: 30px;
            background: white;
            border-top: 1px solid #e0e0e0;
        }

        .btn {
            padding: 12px 30px;
            border: none;
            border-radius: 8px;
            font-size: 1rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s;
            margin: 5px;
        }

        .btn-success {
            background: #48bb78;
            color: white;
        }

        .btn-success:hover {
            background: #38a169;
        }

        .btn-secondary {
            background: #4299e1;
            color: white;
        }

        .btn-secondary:hover {
            background: #3182ce;
        }

        .btn-outline {
            background: white;
            color: #667eea;
            border: 2px solid #667eea;
        }

        .btn-outline:hover {
            background: #667eea;
            color: white;
        }

        @media print {
            body {
                background: white;
                padding: 0;
            }

            .action-buttons {
                display: none !important;
            }

            .certificate-container {
                box-shadow: none;
                border-radius: 0;
                max-width: 100%;
            }

            .certificate {
                page-break-inside: avoid;
            }
        }

        @media (max-width: 768px) {
            .certificate {
                padding: 30px 20px;
            }

            .certificate-border {
                padding: 20px;
                border-width: 10px;
            }

            .certificate-title {
                font-size: 2rem;
                letter-spacing: 2px;
            }

            .recipient-name {
                font-size: 2rem;
                padding: 10px 20px;
            }

            .course-name {
                font-size: 1.5rem;
            }

            .certificate-footer {
                flex-direction: column;
                gap: 30px;
            }

            .signature-line {
                width: 200px;
            }
        }
    </style>
</head>
<body>
    <div class="certificate-container">
        <div class="certificate">
            <div class="certificate-border">
                <div class="certificate-header">
                    <div class="decorative-element">
                        <svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
                            <circle cx="50" cy="50" r="45" fill="none" stroke="currentColor" stroke-width="3"/>
                            <path d="M50 20 L60 40 L80 45 L65 60 L68 80 L50 70 L32 80 L35 60 L20 45 L40 40 Z" fill="currentColor"/>
                        </svg>
                    </div>
                    <h1 class="certificate-title"><?php echo $certificateTitle; ?></h1>
                </div>
                
                <div class="certificate-body">
                    <p class="certificate-text">This is to certify that</p>
                    <div class="recipient-name"><?php echo $recipientName; ?></div>
                    <p class="certificate-text">has successfully completed</p>
                    <h3 class="course-name"><?php echo $courseName; ?></h3>
                    <?php if (!empty($description)): ?>
                        <p class="certificate-description"><?php echo $description; ?></p>
                    <?php endif; ?>
                </div>
                
                <div class="certificate-footer">
                    <div class="signature-section">
                        <div class="signature-line"></div>
                        <p class="issuer-name"><?php echo $issuerName; ?></p>
                        <p class="issuer-title">Authorized Signature</p>
                    </div>
                    <div class="date-section">
                        <p class="date-label">Date</p>
                        <p class="certificate-date"><?php echo $formattedDate; ?></p>
                    </div>
                </div>
            </div>
        </div>

        <div class="action-buttons">
            <button onclick="window.print()" class="btn btn-secondary">🖨️ Print Certificate</button>
            <button onclick="window.history.back()" class="btn btn-outline">← Back</button>
            <button onclick="window.location.href='certificate.php'" class="btn btn-success">➕ Create Another</button>
        </div>
    </div>
</body>
</html>
