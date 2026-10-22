# AI WhatsApp Restaurant Ordering Assistant

## 1. At a glance

| Item | Detail |
| --- | --- |
| Project | AI WhatsApp Restaurant Ordering Assistant |
| What it does | Lets customers view the menu, check availability, ask restaurant questions and place orders on WhatsApp, then saves every confirmed order automatically |
| Built with | n8n, Google Gemini, WhatsApp, Google Sheets, Simple Memory |
| Core idea | Restaurant data lives in Google Sheets, not inside the AI instructions, so the menu can change without editing the workflow |
| Demo | A complete demo shows the flow from customer message to AI processing, menu and FAQ tools, order confirmation and Google Sheets |

## 2. The business problem

Many restaurants take orders through WhatsApp. Someone has to read every message, reply, check what is available, answer the same questions again and again, and write each order down. At busy times this is slow, and mistakes are easy: a sold-out dish gets offered, a quantity is misheard, or a message is missed.

The manual process today:

1. Read each customer message and reply.
2. Check by hand which dishes are available and how many are left.
3. Answer repeated questions about timings, delivery and payment.
4. Note the customer name, items and quantities in a sheet.

## 3. The solution

Optimity Logics built an AI ordering assistant in n8n that talks to customers on WhatsApp. It reads the latest menu and stock from Google Sheets, guides the customer through choosing items, confirms the order, and saves it. A person is not needed to handle every message.

The complete workflow in n8n uses a WhatsApp trigger, an AI Agent with its model, memory and tools, and a reply node.

## 4. How the workflow works

| Step | Node | What it does |
| --- | --- | --- |
| 1 | WhatsApp Trigger | Starts a run each time a customer sends a WhatsApp message |
| 2 | If | Lets only messages that contain text continue; empty or non-text messages stop here |
| 3 | AI Agent | The central node. It reads the message, follows the instructions, decides which tool to call and writes the reply |
| 4 | Google Gemini Chat Model (with a fallback model) | Understands the customer and manages the conversation. The main model retries up to 4 times, 5 seconds apart. If it still fails, a second Gemini model on a separate API account takes over |
| 5 | Simple Memory | Keeps the last 30 messages for each customer, using their WhatsApp number as the session ID, so the assistant does not lose the order |
| 6 | get_inventory | Reads the Inventory sheet (Food Item, Quantity, Status) live every time the menu or stock is needed |
| 7 | get_faq | Reads the FAQ sheet (Question, Answer) to answer restaurant questions |
| 8 | Take-orders | Adds the confirmed order to the Orders sheet with customer name, food item, quantity, status and an automatic order date and time |
| 9 | Send message | Sends the assistant’s reply back to the same customer on WhatsApp |

## 5. How each message is handled

| Customer says | Tool used | What happens |
| --- | --- | --- |
| Asks for the menu, dishes, availability, a specific item, or wants to order | get_inventory | The assistant reads the live inventory, hides unavailable items, groups the rest into numbered categories and then shows numbered items from the chosen category |
| Asks about timings, delivery, payment or policies | get_faq | The answer comes only from the FAQ sheet. If it is not there, the customer is told the information is not available right now |
| Confirms the final order | Take-orders | The order is saved only after the summary is shown and the customer says yes |
| Sends a simple greeting | None | A warm welcome with three options: view menu, place an order, ask a question |

## 6. The customer order journey

1. The customer asks for the menu and the assistant reads the live inventory.
2. Available items are grouped into numbered categories created from the sheet.
3. The customer picks a category number and sees the available items in it. They can also type a dish name directly.
4. The customer picks an item. The assistant asks the quantity and checks it against the stock.
5. The customer can add more items. Earlier items stay in the order.
6. The assistant asks for the customer’s name if it does not have it, then shows the full order summary.
7. The customer confirms. The assistant saves the order and replies that it is placed.

## 7. Key logic: data stays out of the AI instructions

The most important design choice is to keep restaurant data separate from the AI instructions. Instead of writing hundreds of menu items into the prompt, the assistant fetches the latest information from the inventory sheet each time it is needed. The instructions only describe how to behave.

| Situation | Menu written in the prompt | Menu in Google Sheets (used) |
| --- | --- | --- |
| A new dish is added | Edit the prompt and update the workflow | Add a row in the sheet |
| A dish sells out | Edit the prompt | Change its Status in the sheet |
| The menu has hundreds of items | The prompt becomes very long | The prompt stays the same size |
| Accuracy | The AI can use outdated information | The AI reads the latest data every time |

This makes the system more flexible, easier to maintain and better suited to real restaurant operations.

## 8. Google Sheets used

One Google Sheet (Food Delivery System) holds three tabs:

| Tab | Columns | Purpose |
| --- | --- | --- |
| Inventory | Food Item, Quantity, Status | Live menu and availability |
| FAQ | Question, Answer | Restaurant information for customers |
| Orders | Customer Name, Food Item, Quantity Ordered, Order Date, Status | Every confirmed order |

## 9. Tools and technologies

| Tool | Used for | Why |
| --- | --- | --- |
| WhatsApp | Receiving customer messages and sending replies | Customers already use it, so there is nothing new to install |
| n8n | Building and running the workflow | Visual builder with ready connectors and an AI Agent node |
| Google Gemini | Understanding requests and managing the conversation | Handles natural language well; a second model is set up as a fallback |
| Google Sheets | Menu, FAQ and order records | Simple for the restaurant to edit, with no code needed |
| Simple Memory | Conversation context | Remembers recent messages for each customer |

## 10. Safeguards built into the assistant

- **Never invents:** Food items, availability, stock and policies must come from the sheets.
- **Unclear stock is treated as unavailable:** If the status is conflicting, the item is not offered.
- **Stock limit is respected:** If a customer asks for more than is available, the assistant states the real quantity.
- **Confirm before saving:** The full summary is shown first, and the order is saved only after a clear yes.
- **Honest confirmation:** The assistant says the order is placed only after the save succeeds. Cancelled orders are not saved.
- **No technical details:** Tools, sheets and workflow details are never shown to customers. If something fails, the reply is a polite request to try again.

## 11. Limitations and what production needs

- It handles text messages only. Voice notes, images and other message types are ignored.
- Stock is not reduced automatically after an order. The Inventory sheet must be updated separately.
- The Orders sheet has no order ID or customer phone number. Orders with several items should be tested and, in production, saved one row per item with an order ID.
- Payment, delivery address and a notification to the kitchen are not part of this version.
- Google Sheets is a good demo database. Production should use a proper database.
- Simple Memory lives inside n8n. Production should use persistent memory.
- Production also needs error alerts, access control, monitoring and a way to hand over to a human.

## 12. Key learnings and improvements

- **Data outside the prompt:** Keeping data separate from instructions makes the system flexible and easy to maintain.
- **Rules guide the AI:** Clear rules such as check before showing and confirm before saving keep the AI reliable.
- **Plan for failures:** Retries and a fallback model help when the AI service is busy.
- **Next improvements:** Reduce stock automatically after each order, add an order ID and phone number, notify the restaurant team, add payment links, support voice and image messages, and add human hand-off.

---

**Optimity Logics** · info@optimitylogics.com
