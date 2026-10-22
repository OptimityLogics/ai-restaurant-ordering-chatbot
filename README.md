# AI WhatsApp Restaurant Ordering Assistant

An n8n-based conversational workflow that helps restaurants answer customer questions, check menu availability, and record confirmed orders through WhatsApp.

## Overview

The assistant combines Google Gemini with Google Sheets and WhatsApp to support a simple restaurant ordering journey. It can retrieve menu and stock information, answer frequently asked questions, guide customers through item selection, validate requested quantities against available stock, and record an order after customer confirmation.

> This repository contains a sanitized workflow export for learning and demonstration. It is not a hosted service, and it does not include your credentials or live restaurant data.

## Demo

[Watch the workflow demonstration](https://youtu.be/spvmwXP_Aj8?si=wyAeSSaCxCJMbAGc)

## Technology stack

| Component | Purpose |
|---|---|
| n8n | Workflow orchestration and integrations |
| Google Gemini | Conversational understanding and response generation |
| WhatsApp Business Platform | Customer messaging and trigger events |
| Google Sheets | Inventory, FAQ, and order records |
| Simple Memory | Short-term conversation context |
| GitHub Actions | Automated workflow-file validation on pushes and pull requests |

## Repository contents

- `workflow.json` — sanitized n8n workflow export to import into your n8n instance.
- `tests/test_workflow.py` — lightweight structural and security-hygiene checks for the exported workflow.
- `.github/workflows/validate-workflow.yml` — CI workflow that runs the checks on pushes and pull requests.

## Requirements

- An n8n instance with compatible AI Agent, Google Gemini, Google Sheets, and WhatsApp nodes.
- Google Gemini API access.
- WhatsApp Business Platform access and a configured WhatsApp trigger/phone number.
- A Google spreadsheet with `Inventory`, `FAQ`, and `Orders` tabs.

## Google Sheets structure

Use a spreadsheet that matches the fields expected by your workflow. A suggested starting structure is:

| Tab | Example columns |
|---|---|
| `Inventory` | Food Item, Quantity, Status |
| `FAQ` | Question, Answer |
| `Orders` | Customer Name, Food Item, Quantity Ordered, Order Date, Status |

Check the Google Sheets nodes in n8n and align each tab and column with the actual workflow configuration before activating it.

## Setup

1. Download `workflow.json` from this repository.
2. In n8n, open **Workflows** and choose **Import from File**.
3. Select `workflow.json` and review the imported nodes and connections.
4. Add your own Google Gemini, Google Sheets, and WhatsApp credentials in n8n.
5. Replace spreadsheet and WhatsApp placeholders with values from your own environment.
6. Confirm the spreadsheet tabs and columns match the workflow configuration.
7. Test with sample menu questions and order conversations before activating the WhatsApp trigger for real users.
8. Review n8n execution logs and verify that only confirmed orders are recorded as expected.

### Configuration and security

The export is sanitized and uses placeholders for environment-specific settings. Credentials must be added inside your own n8n instance after importing.

- Never commit API keys, access tokens, passwords, webhook secrets, or private customer data.
- Limit access to the workflow and connected spreadsheet to authorized users.
- Test with non-production data first.
- Verify the order-confirmation step and inventory handling before using this workflow in a live restaurant.

## Example conversation

**Customer:** `Show me the available menu.`

**Expected behavior:** The assistant checks the configured inventory data and presents available options based on the connected spreadsheet.

**Customer:** `I want 2 of [available food item].`

**Expected behavior:** The assistant checks availability, continues the order conversation, presents a summary, and asks for confirmation before recording the order.

Actual items, stock levels, and responses depend on the Google Sheets data and the configured model.

## Validation and CI

The repository includes automated checks for JSON validity, expected workflow structure, node connections, and common secret-like values. GitHub Actions runs these checks when changes are pushed or a pull request is opened against the repository.

These checks validate the exported file; they do **not** execute the workflow against live WhatsApp, Gemini, or Google Sheets services. Integration testing must be performed in a configured n8n environment.

## Deployment

This project is an n8n workflow rather than a conventional website, so a website-style auto-deployment pipeline is not applicable by default. The validated JSON can be imported manually into n8n. Automated deployment can be added later if an n8n instance and a securely managed API credential are available; secrets should be stored in GitHub Actions Secrets and never in the repository.

## Limitations

- Requires external accounts, credentials, and a configured Google spreadsheet.
- Conversation quality depends on model configuration and the prompt in the workflow.
- The repository's CI checks do not replace end-to-end tests in n8n.
- Inventory consistency and duplicate-order prevention should be verified for the target restaurant before production use.

## License

No license is currently specified. Contact the repository owner before reusing this project beyond personal evaluation or learning.

---

**Built by [Optimity Logics](https://optimitylogics.com).**
