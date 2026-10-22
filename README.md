# AI WhatsApp Restaurant Ordering Assistant

An AI-powered restaurant ordering assistant built with n8n, Google Gemini, WhatsApp, and Google Sheets.

## 1. Overview

Restaurants often handle menu inquiries, stock checks, customer questions, and order recording manually. This workflow automates these interactions through WhatsApp.

The assistant retrieves live menu and stock information from Google Sheets, answers restaurant FAQs, guides customers through item selection, checks requested quantities, and saves orders after customer confirmation.

## 2. Demo Video

[Watch the AI Restaurant Ordering Chatbot Demo](https://youtu.be/spvmwXP_Aj8?si=wyAeSSaCxCJMbAGc)

## 3. Tech Stack and Tools Used

- **n8n:** Workflow automation and orchestration
- **Google Gemini:** AI-powered conversation and request processing
- **WhatsApp:** Customer messaging
- **Google Sheets:** Inventory, FAQ, and order storage
- **Simple Memory:** Recent conversation context for each customer

## 4. Prerequisites

- An n8n instance with compatible AI Agent, Google Gemini, Google Sheets, and WhatsApp nodes.
- A Google account with access to a spreadsheet.
- Google Gemini API access and credentials.
- WhatsApp Business Platform access and the required API credentials.
- A configured WhatsApp webhook and phone number ID.
- A Google Sheet containing `Inventory`, `FAQ`, and `Orders` tabs.

## 5. Setup Instructions

1. Download `workflow.json` from this repository.
2. Open your n8n instance and navigate to Workflows.
3. Select **Import from File** and choose `workflow.json`.
4. Review the imported nodes and connections.
5. Configure Google Gemini, Google Sheets, and WhatsApp credentials.
6. Update the spreadsheet references and WhatsApp settings for your environment.
7. Configure and activate the WhatsApp trigger, then test the workflow.

## 6. Configuration Details

**Google Gemini**
- Configure valid API credentials for the primary and fallback model nodes.
- Verify the selected models and fallback configuration.

**WhatsApp**
- Configure the WhatsApp Trigger and message-sending node.
- Set the correct phone number ID, credentials, and webhook settings.

**Google Sheets**

Create a spreadsheet with these tabs and columns:

| Tab | Required columns |
|---|---|
| Inventory | Food Item, Quantity, Status |
| FAQ | Question, Answer |
| Orders | Customer Name, Food Item, Quantity Ordered, Order Date, Status |

Update the spreadsheet reference in the inventory, FAQ, and order nodes. The sanitized workflow uses `YOUR_GOOGLE_SHEETS_SPREADSHEET_ID` and `YOUR_WHATSAPP_PHONE_NUMBER_ID` as placeholders. Select the corresponding tabs in your own spreadsheet and configure credentials after importing.

Never commit API keys, access tokens, passwords, or other secrets.

## 7. How to Run the Workflow

1. Import the workflow into n8n.
2. Configure the required credentials and Google Sheets references.
3. Verify that the inventory and FAQ tabs contain the required data.
4. Configure the WhatsApp integration and activate the trigger.
5. Send a text message to the connected WhatsApp number.
6. Test menu browsing, availability checks, FAQ responses, and order confirmation.
7. Review workflow executions and confirm that successfully placed orders appear in the Orders sheet.

## 8. Sample Input and Output

**Sample customer input**

`Show me the available menu.`

**Expected assistant behavior**

The assistant retrieves the current inventory, filters available items, groups them into numbered categories, and asks the customer to select a category.

**Sample ordering interaction**

`I want 2 of [available food item].`

The assistant checks current stock, validates the requested quantity, and continues the order conversation. Before saving, it displays the complete order summary and requests confirmation. After a successful save, it confirms that the order has been recorded.

Actual menu items and availability depend on the connected Google Sheets data.

## 9. Documentation

See [AI WhatsApp Restaurant Ordering Assistant Documentation](AI-WhatsApp-Restaurant-Ordering-Assistant-Documentation.docx) for the business problem, workflow nodes, customer ordering journey, Google Sheets structure, safeguards, limitations, and potential improvements.

## 10. Workflow File

`workflow.json` contains the sanitized n8n workflow export. Credentials, spreadsheet references, and WhatsApp settings must be configured for your own environment before execution.

## 11. Footer

Built by Optimity Logics

#OptimityLogics