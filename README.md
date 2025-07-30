# 💊 Pharmacy Management Module – Odoo 18

A complete solution for managing patient prescriptions 📋 and medicine stock 💼 inside your Odoo medical system.

---

## ✨ Features

- 🧑‍⚕️ Manage patient prescriptions easily.
- 💊 Add multiple medicines per prescription.
- 🔄 Track prescription status: `Draft → Confirmed → Dispensed`.
- 📦 Integrated with inventory to pull medicines from products.
- 🚨 Automatic alerts if stock drops below **Minimum Quantity**.

---

## 🧠 Models

| Model Name                  | Description                           |
|----------------------------|---------------------------------------|
| `pharmacy.prescription`     | Main prescription model               |
| `pharmacy.prescription.line`| Line items for each medicine in prescription |

---

## 📌 Prescription Flow

1. ➕ Create a prescription and add medicines.
2. ✅ Confirm it to validate.
3. 🔍 The system checks stock levels.
4. 📉 If any medicine is below minimum, an alert is generated.
5. 📤 Mark as **Dispensed** when the patient receives their medication.

---

## 🧱 Dependencies

These core Odoo modules are required:

- 📦 `stock` – for inventory management  
- 🛒 `purchase` – for procurement integration  
- 💼 `sale` – for linking with the sales logic  

---

## ⚙️ Installation

1. 📁 Copy the `pharmacy` folder to your **custom addons** directory.
2. 🛠 Restart your Odoo server.
3. 🔄 Update the App List.
4. ✅ Install **Pharmacy Management** from the Apps menu.

---

## 🧪 Usage

- Go to: **Pharmacy → Prescriptions**  
- 📝 Create a new prescription.
- 🧾 Add medicines and select a patient.
- ✔️ Confirm to validate and track stock.
- 🚚 Dispense to mark as completed.
