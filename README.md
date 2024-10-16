﻿# Odoo-17-project

---

# Custom Purchase RFQ - Multi-Vendor Support

## Overview
This module enhances the standard Odoo `purchase.order` (Request for Quotation) functionality by introducing multi-vendor support. It allows users to associate multiple vendors with a purchase order, manage bids, and select a winning bid seamlessly.

## Features
- **Multiple Vendors:** Allows the selection of multiple vendors for a single purchase order.
- **Bid Management:** Adds the ability to track bids from different vendors directly within the purchase order.
- **Winning Bid Selection:** Introduces functionality to select a winning bid, which automatically assigns the vendor to the purchase order.

## Installation
1. Place the module folder in your Odoo custom add-ons directory.
2. Ensure that the `purchase` module is installed as it is a dependency.
3. Update your Odoo instance:
   ```bash
   ./odoo-bin -c odoo.conf -u custom_purchase_rfq
   ```
4. Restart the Odoo server:
   ```bash
   sudo systemctl restart odoo
   ```

## Usage
### Multi-Vendor Selection
- When creating a new RFQ, you'll now see a field labeled **Vendors** instead of the traditional **Vendor** field. This allows you to select multiple vendors for the purchase order.

### Bid Management
- In the RFQ form, a new **Bids** section is added. Users can input bids from various vendors, including vendor names, bid prices, and bid dates.

### Winning Bid Confirmation
- After receiving bids, select a winning bid by using the **Winning Bid** field.
- To confirm the winning bid, click on the **Confirm Winning Bid** button, which will assign the winning vendor to the purchase order and update its state to 'purchase.'

## Technical Details
### Model Extensions
- **Fields Added:**
  - `vendor_ids`: Many2many field linking to multiple vendors.
  - `bid_ids`: One2many field linking to the `purchase.bid` model for managing bids.
  - `winning_bid_id`: Many2one field to track the selected winning bid.
  



---

