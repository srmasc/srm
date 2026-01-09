<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Certificate Generator</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
            color: #333;
        }

        .container {
            max-width: 800px;
            margin: 0 auto;
        }

        header {
            text-align: center;
            color: white;
            margin-bottom: 40px;
            padding: 20px;
        }

        header h1 {
            font-size: 3rem;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }

        header p {
            font-size: 1.2rem;
            opacity: 0.9;
        }

        .form-section {
            background: white;
            border-radius: 15px;
            padding: 40px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }

        .form-section h2 {
            color: #667eea;
            margin-bottom: 30px;
            font-size: 1.8rem;
        }

        .form-group {
            margin-bottom: 25px;
        }

        .form-group label {
            display: block;
            margin-bottom: 8px;
            font-weight: 600;
            color: #555;
            font-size: 1rem;
        }

        .form-group input,
        .form-group textarea,
        .form-group select {
            width: 100%;
            padding: 12px;
            border: 2px solid #e0e0e0;
            border-radius: 8px;
            font-size: 1rem;
            transition: border-color 0.3s;
            font-family: inherit;
        }

        .form-group input:focus,
        .form-group textarea:focus,
        .form-group select:focus {
            outline: none;
            border-color: #667eea;
        }

        .form-group textarea {
            resize: vertical;
            min-height: 80px;
        }

        .btn {
            padding: 15px 40px;
            border: none;
            border-radius: 8px;
            font-size: 1.1rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s;
            width: 100%;
            background: #667eea;
            color: white;
        }

        .btn:hover {
            background: #5568d3;
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
        }

        footer {
            text-align: center;
            color: white;
            padding: 20px;
            margin-top: 20px;
            opacity: 0.8;
        }

        .required {
            color: #e53e3e;
        }

        @media (max-width: 768px) {
            header h1 {
                font-size: 2rem;
            }

            .form-section {
                padding: 25px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>🎓 Certificate Generator</h1>
            <p>Create beautiful certificates in seconds</p>
        </header>

        <div class="form-section">
            <h2>Enter Certificate Details</h2>
            <form action="generate.php" method="POST" target="_blank">
                <div class="form-group">
                    <label for="recipientName">Recipient Name <span class="required">*</span></label>
                    <input type="text" id="recipientName" name="recipientName" placeholder="John Doe" required>
                </div>

                <div class="form-group">
                    <label for="courseName">Course/Achievement <span class="required">*</span></label>
                    <input type="text" id="courseName" name="courseName" placeholder="Web Development" required>
                </div>

                <div class="form-group">
                    <label for="issuerName">Issued By <span class="required">*</span></label>
                    <input type="text" id="issuerName" name="issuerName" placeholder="Organization Name" required>
                </div>

                <div class="form-group">
                    <label for="date">Date <span class="required">*</span></label>
                    <input type="date" id="date" name="date" value="<?php echo date('Y-m-d'); ?>" required>
                </div>

                <div class="form-group">
                    <label for="description">Description (Optional)</label>
                    <textarea id="description" name="description" placeholder="For outstanding performance in..."></textarea>
                </div>

                <div class="form-group">
                    <label for="certificateType">Certificate Type</label>
                    <select id="certificateType" name="certificateType">
                        <option value="achievement">Certificate of Achievement</option>
                        <option value="completion">Certificate of Completion</option>
                        <option value="appreciation">Certificate of Appreciation</option>
                        <option value="excellence">Certificate of Excellence</option>
                    </select>
                </div>

                <button type="submit" class="btn">Generate Certificate</button>
            </form>
        </div>
    </div>

    <footer>
        <p>&copy; <?php echo date('Y'); ?> Certificate Generator. Made with ❤️</p>
    </footer>
</body>
</html>
