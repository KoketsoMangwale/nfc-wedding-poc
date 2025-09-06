# NFC Wedding PoC

Serverless NFC Wedding Proof-of-Concept (PoC) using AWS SAM, Lambda, DynamoDB, S3, and CloudFront.  
This project demonstrates a modern, interactive wedding experience with NFC cards and wristbands.

## Features
- Guest verification & RSVP tracking via NFC.
- Personalized table assignment.
- Digital wedding program accessible via NFC card.
- Gift registry access through NFC card.
- Thank-you video wristband delivered post-wedding.

## Architecture
1. Guest taps NFC card → unique URL triggers **API Gateway**.
2. **Lambda** fetches guest data from **DynamoDB**.
3. Lambda redirects guest to **CloudFront-hosted S3 content**.
4. Tap event logged in DynamoDB for analytics.

## AWS Resources
- **Lambda Function**: Handles guest requests and personalization.
- **API Gateway**: Provides unique endpoints for each guest.
- **DynamoDB Table**: Stores guest info, RSVP, table assignment, tap counts.
- **S3 Bucket**: Stores wedding content (photos, program, videos, playlists).
- **CloudFront Distribution**: Delivers content quickly and securely.

## Project Structure
```

nfc-wedding-poc/
├─ README.md                  # Project overview, setup instructions, usage
├─ template.yaml              # AWS SAM template (Lambda, API Gateway, DynamoDB, S3, CloudFront)
├─ src/
│   └─ app.py                 # Lambda function handler
├─ content/
│   ├─ index.html             # Landing page / default page
│   ├─ gift_registry.html     # Demo gift registry page
│   ├─ program.html           # Demo program page
│   └─ thank_you.mp4          # Demo thank-you video
├─ .gitignore                 # Ignore Python/IDE artifacts
└─ requirements.txt           # Python dependencies (if needed, e.g., boto3)

````

## Getting Started

### Prerequisites
- AWS CLI configured
- AWS SAM CLI installed
- Python 3.11

### Deploy
```bash
sam build
sam deploy --guided
````

### Programming NFC Cards

* Use the API Gateway endpoint from deployment.
* Program each NFC card/wristband with a unique URL including `guest_id` parameter:

```
https://<api-gateway-url>/prod/guest?guest_id=GUEST001
```

### Demo Content

* Upload sample wedding pages to `content/` folder.
* CloudFront serves content to guests when NFC card is tapped.

## Contributing

* Fork the repository, submit PRs for improvements or additional features (e.g., Spotify playlist integration, dynamic menu updates, analytics dashboard).

## License

MIT License


---

## **.gitignore Example**
```
**pycache**/
\*.pyc
.env
\*.log
.aws-sam/

```

---

## **requirements.txt** (Optional, if using additional Python packages)
```

boto3

```

---

