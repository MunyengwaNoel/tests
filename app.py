from flask import Flask, jsonify
from flask import request
import uuid
import os
from werkzeug.utils import secure_filename
import random
import string

from pydantic import BaseModel, ValidationError, Field
from typing import List
# from datetime import datetime
from datetime import datetime, timedelta


from datetime import datetime

app = Flask(__name__)


@app.route('/insurance/list/LifeInsurance', methods=['GET'])
def get_subscribed_policies():
    return jsonify(subsrcibed_policies)


@app.route('/funeral-policies', methods=['GET'])
def get_policy():
    return jsonify(policies)


@app.route("/insurance/switch/submit", methods=["POST"])
def submit_policy_change():
    data = request.get_json()

    if not data or "policyChangeId" not in data:
        return jsonify({
            "success": False,
            "message": "policyChangeId is required"
        }), 400

    policy_change_id = data.get("policyChangeId")

    response = {
        "success": True,
        "data": {
            "message": "Policy change submitted successfully.",
            "policyChangeId": policy_change_id
        },
        "message": "Policy change submitted successfully."
    }

    return jsonify(response), 200

@app.route('/flex-policies', methods=['GET'])
def get_flex_policy():
    return jsonify(new_flex_policies)




# -------------------------
# MODELS
# -------------------------

class FuneralDependantModel(BaseModel):
    dependantId: str
    newPolicyId: str

class FuneralSwitchRequest(BaseModel):
    insuranceId: str
    newPolicyId: str
    immediate: bool
    effective: str = Field(..., description="Effective date")
    changeType: str
    dependants: List[FuneralDependantModel]
    class Config:
        extra = "forbid"  # ❌ no unknown fields


class FlexDependantModel(BaseModel):
    dependantId: str
    coverAmount: float = Field(..., ge=0, description="Cover amount must be >= 0")

class FlexSwitchRequest(BaseModel):
    insuranceId: str
    coverAmount: float = Field(..., ge=0, description="Cover amount must be >= 0")
    immediate: bool
    effective: str = Field(..., description="Effective date")
    
    changeType: str
    dependants: List[FlexDependantModel]
    class Config:
        extra = "forbid"  # ❌ no unknown fields


# -------------------------
# ENDPOINTS
# -------------------------

@app.route('/insurance/switch/funeral', methods=['POST'])
def switch_funeral_insurance():
    print(request.get_json())
    try:
        body = FuneralSwitchRequest(**request.get_json())
    except ValidationError as e:
        return jsonify({
            "success": False,
            "message": "Invalid request body",
            "errors": e.errors()
        }), 400

    response = {
        "success": True,
        "data": {
            "status": "success",
            "policyChangeId": str(uuid.uuid4()),
            "message": "Policy upgrade request processed successfully.",
            "changeType": body.changeType,
            "previousPremium": "5.50",
            "newPremium": 11,
            "effectiveDate": "2025-07-10",
            "policyChanges": {
                "fromPolicy": {
                    "id": "192dc7d9-3656-4253-812d-47024855c76e",
                    "name": "Lite",
                    "type": "FuneralPlan",
                    "coverageAmount": "2.75"
                },
                "toPolicy": {
                    "id": "fcd475af-7781-461a-8a75-5c78c1abd5ac",
                    "name": "Classic",
                    "type": "FuneralPlan",
                    "coverageAmount": "5.50"
                }
            },
            "dependantChanges": [
                {
                    "dependantId": "94978713-f147-4285-b5a8-78534a8cf479",
                    "dependantName": "Layla",
                    "fromPolicy": {
                        "id": "192dc7d9-3656-4253-812d-47024855c76e",
                        "name": "Lite",
                        "type": "FuneralPlan",
                        "coverageAmount": "2.75"
                    },
                    "toPolicy": {
                        "id": "fcd475af-7781-461a-8a75-5c78c1abd5ac",
                        "name": "Classic",
                        "type": "FuneralPlan",
                        "coverageAmount": "5.50"
                    },
                    "premiumDifference": 2.75
                }
            ],
            "timestamp": "2025-07-10 13:00:16"
        },
        "message": "Operation successful"
    }

    return jsonify(response), 200



def generate_flex_reference(prefix="FLE"):
    """Generate a random reference like FLE-QGYOSDUKKS"""
    random_part = ''.join(random.choices(string.ascii_uppercase, k=10))
    return f"{prefix}-{random_part}"


@app.route('/insurance/attach/dependants', methods=['POST'])
def attach_dependants():
    try:
        data = request.get_json()

        # ✅ Validate input
        if not data or "insuranceId" not in data or "dependants" not in data:
            return jsonify({
                "success": False,
                "message": "Invalid request. 'insuranceId' and 'dependants' are required."
            }), 400

        insurance_id = data.get("insuranceId")
        dependants = data.get("dependants", [])

        # Example existing dependants (for demonstration)
        existing_dependants = [
            {
                "id": "e2303263-b074-4044-84d8-16ad7b6ed7f1",
                "user_id": "d2f52404-1041-701e-e810-4dc57855f83d",
                "gender": "male",
                "title": "Mr",
                "relationship": "Brother",
                "first_name": "James",
                "last_name": "Murphy",
                "national_id": "1400009M12",
                "date_of_birth": "1980-06-20T00:00:00.000000Z",
                "phone_number": "+263712252252",
                "province": "Midlands",
                "address": "44 Mainway Meadows",
                "pivot": {
                    "insurable_type": "App\\Models\\LifeInsurance",
                    "insurable_id": insurance_id,
                    "dependant_id": "e2303263-b074-4044-84d8-16ad7b6ed7f1",
                    "cover_amount": "1116.01",
                    "coverage_amount": "2.01",
                    "is_primary": True,
                    "relationship_type": "Brother",
                    "policy_id": "6fb41a4e-7e62-4b84-8951-f701bf6cbae0",
                    "policy_type": "App\\Models\\FlexPlan",
                    "created_at": "2025-06-18T08:27:42.000000Z",
                    "updated_at": "2025-06-18T08:27:42.000000Z"
                }
            },
            {
                "id": "4a07ad72-f6cb-4059-babc-41583f6d2632",
                "user_id": "d2f52404-1041-701e-e810-4dc57855f83d",
                "gender": "male",
                "title": "Mrs",
                "relationship": "Wifey",
                "first_name": "Layla",
                "last_name": "Murphy",
                "national_id": "1500009M12",
                "date_of_birth": "1990-06-20T00:00:00.000000Z",
                "phone_number": "+263712252009",
                "province": "Midlands",
                "address": "44 Mainway Meadows",
                "pivot": {
                    "insurable_type": "App\\Models\\LifeInsurance",
                    "insurable_id": insurance_id,
                    "dependant_id": "4a07ad72-f6cb-4059-babc-41583f6d2632",
                    "cover_amount": "1180.00",
                    "coverage_amount": "2.12",
                    "is_primary": True,
                    "relationship_type": "Wifey",
                    "policy_id": "6fb41a4e-7e62-4b84-8951-f701bf6cbae0",
                    "policy_type": "App\\Models\\FlexPlan",
                    "created_at": "2025-06-30T10:01:52.000000Z",
                    "updated_at": "2025-06-30T10:01:52.000000Z"
                }
            }
        ]

        # ✅ Simulate attaching new dependants
        new_dependants = []
        for dep in dependants:
            dependant_id = dep.get("dependantId")
            cover_amount = dep.get("coverAmount")
            coverage_amount = str(round(float(cover_amount) / 667, 2))  # demo calc

            new_dependants.append({
                "id": dependant_id,
                "user_id": "d2f52404-1041-701e-e810-4dc57855f83d",
                "gender": "male",
                "title": "Miss",
                "relationship": "Daughter",
                "first_name": "Elen",
                "last_name": "Murphy",
                "national_id": "1700009M12",
                "date_of_birth": "2015-06-20T00:00:00.000000Z",
                "province": "Midlands",
                "address": "44 Mainway Meadows",
                "pivot": {
                    "insurable_type": "App\\Models\\LifeInsurance",
                    "insurable_id": insurance_id,
                    "dependant_id": dependant_id,
                    "cover_amount": cover_amount,
                    "coverage_amount": coverage_amount,
                    "is_primary": True,
                    "relationship_type": "Daughter",
                    "policy_id": str(uuid.uuid4()),
                    "policy_type": "App\\Models\\FlexPlan",
                    "created_at": datetime.utcnow().isoformat() + "Z",
                    "updated_at": datetime.utcnow().isoformat() + "Z"
                }
            })

        # Merge existing + new
        all_dependants = existing_dependants + new_dependants

        # ✅ Construct main insurance object
        insurance_data = {
            "id": insurance_id,
            "user_id": "d2f52404-1041-701e-e810-4dc57855f83d",
            "policy_number": None,
            "policy_ref_number": "685278B31588F",
            "currency": "USD",
            "premium_amount": 8.72,
            "cover_amount": "1567.00",
            "with_bus": False,
            "quotation_id": "50921780-1a5f-4f22-9aa9-b2c193089425",
            "status": "ACTIVE",
            "policy_type": "FLEX",
            "plan_id": "6fb41a4e-7e62-4b84-8951-f701bf6cbae0",
            "plan_type": "App\\Models\\FlexPlan",
            "activated_at": "2025-06-18T08:28:35.000000Z",
            "expires_at": "2026-06-18T08:28:35.000000Z",
            "created_at": "2025-06-18T08:27:42.000000Z",
            "updated_at": datetime.utcnow().isoformat() + "Z",
            "dependants": all_dependants
        }

        response = {
            "success": True,
            "data": insurance_data,
            "message": "Dependants attached successfully."
        }

        return jsonify(response), 200

    except Exception as e:
        return jsonify({
            "success": False,
            "message": str(e)
        }), 500



@app.route('/insurance/flex/process', methods=['POST'])
def process_flex_insurance():
    try:
        data = request.get_json()

        # ✅ Validate request
        if not data or "quotationId" not in data or "paymentDetails" not in data:
            return jsonify({
                "success": False,
                "message": "Invalid request body. 'quotationId' and 'paymentDetails' are required."
            }), 400

        quotation_id = data.get("quotationId")
        payment_details = data.get("paymentDetails", {})
        payment_method = payment_details.get("paymentMethod", "")
        account_number = payment_details.get("accountNumber", "")

        # ✅ Generate dynamic fields
        reference_code = generate_flex_reference()
        transaction_id = str(uuid.uuid4())
        insurance_id = str(uuid.uuid4())
        payment_id = str(uuid.uuid4())
        internal_ref = ''.join(random.choices('0123456789ABCDEF', k=30))
        external_ref = f"{account_number[-9:]}{datetime.utcnow().strftime('%d%m%H%M%S%f')[:12]}"

        # ✅ Construct response
        response = {
            "success": True,
            "data": {
                "status": "PENDING",
                "message": reference_code,
                "transactionId": transaction_id,
                "insuranceId": insurance_id,
                "amount": "4.83",
                "currency": "890",
                "paymentId": payment_id,
                "checkoutId": None,
                "checkoutNdc": None,
                "buildNumber": None,
                "description": reference_code,
                "paymentMethod": payment_method,
                "internalReference": internal_ref,
                "externalReference": external_ref
            },
            "message": reference_code
        }

        return jsonify(response), 200

    except Exception as e:
        return jsonify({
            "success": False,
            "message": str(e)
        }), 500


@app.route('/insurance/flex/quotation', methods=['POST'])
def flex_quotation():
    try:
        data = request.get_json()

        # ✅ Validate input
        if not data or 'currencyCode' not in data or 'coverAmount' not in data:
            return jsonify({"success": False, "message": "Invalid request body"}), 400

        currency_code = data.get("currencyCode")
        cover_amount = data.get("coverAmount")
        dependants = data.get("dependants", [])

        # Constants for demo
        user_id = "c2759474-10a1-706e-cbaf-542d48eb1aa6"
        policy_id = "9c3f0e47-d6c7-4948-897f-3bd201b213fa"
        premium_rate = 1.80
        min_payout = 1000.00
        currency = "USD"

        # Calculate main policy premium
        main_premium = round((cover_amount * premium_rate) / min_payout, 2)

        # Calculate dependants premiums
        dependants_list = []
        dependants_total = 0.0
        for dep in dependants:
            dep_cover = dep.get("coverAmount", 0)
            dep_premium = round((dep_cover * premium_rate) / min_payout, 2)
            dependants_total += dep_premium
            dependants_list.append({
                "age": 19,  # example fixed
                "policy_id": policy_id,
                "cover_amount": dep_cover,
                "premium_amount": dep_premium,
                "premium_rate": f"{premium_rate:.2f}",
                "min_payout": f"{min_payout:.2f}",
                "currency_code": currency,
                "coverAmount": dep_cover,
                "dependantId": dep.get("dependantId")
            })

        # Total premium
        total_premium = round(main_premium + dependants_total, 2)

        # Response construction
        response = {
            "success": True,
            "data": {
                "id": str(uuid.uuid4()),
                "userId": user_id,
                "service": "LIFE",
                "serviceType": "FLEX",
                "currencyCode": currency_code,
                "totalAmount": f"{total_premium:.2f}",
                "monthsInsured": 1,
                "premium": f"{total_premium:.2f}",
                "stampDuty": None,
                "expiresAt": (datetime.utcnow() + timedelta(days=30)).isoformat() + "Z",
                "status": "pending",
                "metadata": {
                    "main_policy": {
                        "age": 58,
                        "policy_id": policy_id,
                        "cover_amount": cover_amount,
                        "premium_amount": main_premium,
                        "premium_rate": f"{premium_rate:.2f}",
                        "min_payout": f"{min_payout:.2f}",
                        "currency_code": currency,
                        "userId": user_id,
                        "currency": currency,
                        "coverAmount": cover_amount
                    },
                    "dependants": dependants_list,
                    "calculation_details": {
                        "formula": "(cover_amount * premium_rate) / min_payout",
                        "example": f"({cover_amount} * {premium_rate}) / {min_payout:.2f} = {main_premium}"
                    }
                },
                "request": {
                    "userId": user_id,
                    "currencyCode": currency_code,
                    "coverAmount": cover_amount,
                    "dependants": dependants,
                    "currency": currency
                },
                "createdAt": datetime.utcnow().isoformat() + "Z",
                "updatedAt": datetime.utcnow().isoformat() + "Z"
            },
            "message": "Quotation generated successfully"
        }

        return jsonify(response), 200

    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500








def generate_reference(prefix="FLE"):
    """Generate a random internal reference like FLE-QGYOSDUKKS"""
    random_part = ''.join(random.choices(string.ascii_uppercase, k=10))
    return f"{prefix}-{random_part}"

@app.route('/insurance/flex/payment', methods=['POST'])
def flex_payment():
    try:
        data = request.get_json()

        # ✅ Validate input
        if not data or "quotationId" not in data or "paymentDetails" not in data:
            return jsonify({"success": False, "message": "Invalid request body"}), 400
        
        quotation_id = data.get("quotationId")
        payment_details = data.get("paymentDetails", {})
        payment_method = payment_details.get("paymentMethod")
        account_number = payment_details.get("accountNumber")

        # ✅ Generate dynamic fields
        reference_code = generate_reference()
        transaction_id = str(uuid.uuid4())
        insurance_id = str(uuid.uuid4())
        payment_id = str(uuid.uuid4())
        internal_ref = ''.join(random.choices('0123456789ABCDEF', k=30))
        external_ref = f"{account_number[-9:]}{datetime.utcnow().strftime('%d%m%H%M%S%f')[:12]}"

        response = {
            "success": True,
            "data": {
                "status": "PENDING",
                "message": reference_code,
                "transactionId": transaction_id,
                "insuranceId": insurance_id,
                "amount": "4.83",
                "currency": "890",
                "paymentId": payment_id,
                "checkoutId": None,
                "checkoutNdc": None,
                "buildNumber": None,
                "description": reference_code,
                "paymentMethod": payment_method,
                "internalReference": internal_ref,
                "externalReference": external_ref
            },
            "message": reference_code
        }

        return jsonify(response), 200

    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500





@app.route('/insurance/switch/flex', methods=['POST'])
def switch_flex_insurance():
    print(request.get_json())
    try:
        body = FlexSwitchRequest(**request.get_json())
    except ValidationError as e:
        return jsonify({
            "success": False,
            "message": "Invalid request body",
            "errors": e.errors()
        }), 400

    response = {
        "success": True,
        "data": {
            "status": "success",
            "policyChangeId": str(uuid.uuid4()),
            "message": f"Policy {body.changeType} request processed successfully.",
            "changeType": body.changeType,
            "previousPremium": "4.49",
            "newPremium": 5.85,
            "effectiveDate": "2025-07-10",
            "currency": "USD",
            "policyChanges": {
                "fromPolicy": {
                    "id": "4b8e211a-9c7c-4b17-9ca9-d23c48d11811",
                    "type": "App\\Models\\FlexPlan",
                    "coverageAmount": "1567.00",
                    "premiumAmount": "4.49"
                },
                "toPolicy": {
                    "id": "4b8e211a-9c7c-4b17-9ca9-d23c48d11811",
                    "type": "App\\Models\\FlexPlan",
                    "coverageAmount": body.coverAmount,
                    "premiumAmount": 5.85
                }
            },
            "dependantChanges": [
                {
                    "dependantId": "15878c4b-1d04-4e51-a548-f57083e04c8f",
                    "dependantName": "Elen",
                    "fromPolicy": {
                        "id": "82ad8099-bacb-4b2d-b080-41220fa2a0a8",
                        "type": "App\\Models\\FlexPlan",
                        "coverAmount": "1116.01",
                        "premiumAmount": "1.67"
                    },
                    "toPolicy": {
                        "id": "82ad8099-bacb-4b2d-b080-41220fa2a0a8",
                        "type": "App\\Models\\FlexPlan",
                        "coverAmount": body.dependants[0].coverAmount,
                        "premiumAmount": 2.25
                    },
                    "premiumDifference": 0.58
                }
            ],
            "timestamp": "2025-07-10 12:50:04"
        },
        "message": "Operation successful"
    }

    return jsonify(response), 200

# @app.route("/insurance/switch/flex", methods=["POST"])
# def upgrade_flex_policy():
#     try:
#         data = request.get_json()

#         insurance_id = data.get("insuranceId")
#         new_cover_amount = data.get("coverAmount")
#         immediate = data.get("immediate", False)
#         effective_date_str = data.get("effective")
#         change_type = data.get("changeType", "UPGRADE")
#         dependants = data.get("dependants", [])

#         # Simulated previous policy
#         from_policy_main = {
#             "id": "4b8e211a-9c7c-4b17-9ca9-d23c48d11811",
#             "type": "App\\Models\\FlexPlan",
#             "coverageAmount": "1567.00",
#             "premiumAmount": "4.49"
#         }

#         to_policy_main = {
#             "id": from_policy_main["id"],
#             "type": from_policy_main["type"],
#             "coverageAmount": new_cover_amount,
#             "premiumAmount": 5.85  # Simulated premium for new cover amount
#         }

#         # Simulated previous premium
#         previous_premium = float(from_policy_main["premiumAmount"])
#         new_premium = to_policy_main["premiumAmount"]

#         # Process dependant changes
#         dependant_changes = []
#         for dep in dependants:
#             dependant_changes.append({
#                 "dependantId": dep.get("dependantId"),
#                 "dependantName": "Elen",  # Normally fetched from DB
#                 "fromPolicy": {
#                     "id": "82ad8099-bacb-4b2d-b080-41220fa2a0a8",
#                     "type": "App\\Models\\FlexPlan",
#                     "coverAmount": "1116.01",
#                     "premiumAmount": "1.67"
#                 },
#                 "toPolicy": {
#                     "id": "82ad8099-bacb-4b2d-b080-41220fa2a0a8",
#                     "type": "App\\Models\\FlexPlan",
#                     "coverAmount": dep.get("coverAmount"),
#                     "premiumAmount": 2.25  # Simulated premium for new cover amount
#                 },
#                 "premiumDifference": round(2.25 - 1.67, 2)
#             })

#         # Effective date formatting
#         effective_date = datetime.fromisoformat(effective_date_str).date() if effective_date_str else (datetime.utcnow() + timedelta(days=1)).date()

#         response = {
#             "success": True,
#             "data": {
#                 "status": "success",
#                 "policyChangeId": str(uuid.uuid4()),
#                 "message": f"Policy {change_type} request processed successfully.",
#                 "changeType": change_type,
#                 "previousPremium": f"{previous_premium:.2f}",
#                 "newPremium": new_premium,
#                 "effectiveDate": str(effective_date),
#                 "currency": "USD",
#                 "policyChanges": {
#                     "fromPolicy": from_policy_main,
#                     "toPolicy": to_policy_main
#                 },
#                 "dependantChanges": dependant_changes,
#                 "timestamp": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
#             },
#             "message": "Operation successful"
#         }

#         return jsonify(response), 201

#     except Exception as e:
#         return jsonify({"success": False, "message": str(e)}), 500


@app.route("/insurance/funeral/process", methods=["POST"])
def buy_funeral_insurance():
    try:
        data = request.get_json()

        # Extract required fields from request body
        user_id = data.get("userId")
        currency_code = data.get("currencyCode")
        funeral_policy_id = data.get("funeralPolicyId")
        dependants = data.get("dependants", [])
        payment_details = data.get("paymentDetails", {})

        # Mock logic - in production, you'd validate, compute amount, store in DB, etc.
        # For now, simulate a fixed result:
        response = {
            "success": True,
            "data": {
                "status": "PENDING",
                "message": None,
                "transaction_id": 2,
                "insurance_id": 2,
                "amount": 11.25,
                "currency": currency_code,
                "payment_id": 2,
                "checkout_id": None,
                "checkout_ndc": None,
                "build_number": None,
                "description": None,
                "payment_method": "EcoCash",
                "internal_reference": "f8410984db774555B685DD933D3CB62A",
                "external_reference": "783797406250422084416332"
            },
            "message": None
        }

        return jsonify(response), 201

    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500





# ---------- Validation Models ----------
class DependantModel(BaseModel):
    dependantId: str
    newPolicyId: str

class InsuranceSwitchRequest(BaseModel):
    insuranceId: str
    newPolicyId: str
    immediate: bool
    effective: str
    changeType: str
    dependants: List[DependantModel]

    class Config:
        extra = "forbid"  # ❌ forbid extra/unknown fields


# # ---------- Endpoint ----------
# @app.route('/insurance/switch/funeral', methods=['POST'])
# def switch_funeral_insurance():
#     try:
#         # Validate incoming JSON strictly
#         data = InsuranceSwitchRequest(**request.get_json())

#     except ValidationError as e:
#         # Return validation errors clearly
#         return jsonify({
#             "success": False,
#             "message": "Invalid request body",
#             "errors": e.errors()
#         }), 400

#     # Simulate processing logic
#     policy_change_id = str(uuid.uuid4())
#     timestamp = datetime(2025, 7, 10, 13, 0, 16).strftime("%Y-%m-%d %H:%M:%S")

#     response = {
#         "success": True,
#         "data": {
#             "status": "success",
#             "policyChangeId": policy_change_id,
#             "message": "Policy upgrade request processed successfully.",
#             "changeType": data.changeType,
#             "previousPremium": "5.50",
#             "newPremium": 11,
#             "effectiveDate": "2025-07-10",
#             "policyChanges": {
#                 "fromPolicy": {
#                     "id": "192dc7d9-3656-4253-812d-47024855c76e",
#                     "name": "Lite",
#                     "type": "FuneralPlan",
#                     "coverageAmount": "2.75"
#                 },
#                 "toPolicy": {
#                     "id": "fcd475af-7781-461a-8a75-5c78c1abd5ac",
#                     "name": "Classic",
#                     "type": "FuneralPlan",
#                     "coverageAmount": "5.50"
#                 }
#             },
#             "dependantChanges": [
#                 {
#                     "dependantId": "94978713-f147-4285-b5a8-78534a8cf479",
#                     "dependantName": "Layla",
#                     "fromPolicy": {
#                         "id": "192dc7d9-3656-4253-812d-47024855c76e",
#                         "name": "Lite",
#                         "type": "FuneralPlan",
#                         "coverageAmount": "2.75"
#                     },
#                     "toPolicy": {
#                         "id": "fcd475af-7781-461a-8a75-5c78c1abd5ac",
#                         "name": "Classic",
#                         "type": "FuneralPlan",
#                         "coverageAmount": "5.50"
#                     },
#                     "premiumDifference": 2.75
#                 }
#             ],
#             "timestamp": timestamp
#         },
#         "message": "Operation successful"
#     }

#     return jsonify(response), 200


# @app.route("/insurance/switch/funeral", methods=["POST"])
# def upgrade_policy():
#     try:
#         data_list = request.get_json()
        
#         if not isinstance(data_list, list):
#             return jsonify({"success": False, "message": "Request body must be a list of policy changes."}), 400

#         results = []

#         for data in data_list:
#             insurance_id = data.get("insuranceId")
#             new_policy_id = data.get("newPolicyId")
#             immediate = data.get("immediate", False)
#             effective = data.get("effective")
#             change_type = data.get("changeType", "UPGRADE")
#             dependants = data.get("dependants", [])
#             selected_dependants = data.get("selectedDependants", [])

#             # Simulate previous and new premiums
#             previous_premium = 5.50
#             new_premium = 11

#             # Simulate previous and new policies
#             from_policy = {
#                 "id": "192dc7d9-3656-4253-812d-47024855c76e",
#                 "name": "Lite",
#                 "type": "FuneralPlan",
#                 "coverageAmount": "2.75"
#             }

#             to_policy = {
#                 "id": new_policy_id,
#                 "name": "Classic",
#                 "type": "FuneralPlan",
#                 "coverageAmount": "5.50"
#             }

#             # Process dependants changes
#             dependant_changes = []
#             for dep in dependants:
#                 if dep.get("dependantId") in selected_dependants:
#                     dependant_changes.append({
#                         "dependantId": dep.get("dependantId"),
#                         "dependantName": "Layla",  # Normally fetched from DB
#                         "fromPolicy": from_policy,
#                         "toPolicy": to_policy,
#                         "premiumDifference": float(to_policy["coverageAmount"]) - float(from_policy["coverageAmount"])
#                     })

#             # Effective date
#             effective_date = datetime.fromisoformat(effective.replace("Z", "+00:00")).date() if effective else (datetime.utcnow() + timedelta(days=1)).date()

#             results.append({
#                 "status": "success",
#                 "policyChangeId": str(uuid.uuid4()),
#                 "message": "Policy upgrade request processed successfully.",
#                 "insuranceId": insurance_id,
#                 "changeType": change_type,
#                 "previousPremium": str(previous_premium),
#                 "newPremium": new_premium,
#                 "effectiveDate": str(effective_date),
#                 "policyChanges": {
#                     "fromPolicy": from_policy,
#                     "toPolicy": to_policy
#                 },
#                 "dependantChanges": dependant_changes,
#                 "timestamp": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
#             })

#         return jsonify({
#             "success": True,
#             "data": results,
#             "message": "All policy upgrades processed successfully."
#         }), 201

#     except Exception as e:
#         return jsonify({"success": False, "message": str(e)}), 500


# @app.route("/insurance/switch/funeral", methods=["POST"])
# def upgrade_policy():
#     try:
#         data = request.get_json()

#         insurance_id = data.get("insuranceId")
#         new_policy_id = data.get("newPolicyId")
#         immediate = data.get("immediate", False)
#         effective = data.get("effective")
#         change_type = data.get("changeType", "UPGRADE")
#         dependants = data.get("dependants", [])

#         # Simulate previous and new premiums
#         previous_premium = 5.50
#         new_premium = 11

#         # Simulate previous and new policies
#         from_policy = {
#             "id": "192dc7d9-3656-4253-812d-47024855c76e",
#             "name": "Lite",
#             "type": "FuneralPlan",
#             "coverageAmount": "2.75"
#         }

#         to_policy = {
#             "id": new_policy_id,
#             "name": "Classic",
#             "type": "FuneralPlan",
#             "coverageAmount": "5.50"
#         }

#         # Process dependants changes
#         dependant_changes = []
#         for dep in dependants:
#             dependant_changes.append({
#                 "dependantId": dep.get("dependantId"),
#                 "dependantName": "Layla",  # Normally fetched from DB
#                 "fromPolicy": from_policy,
#                 "toPolicy": to_policy,
#                 "premiumDifference": float(to_policy["coverageAmount"]) - float(from_policy["coverageAmount"])
#             })

#         # Effective date formatting
#         effective_date = datetime.fromisoformat(effective.replace("Z", "+00:00")).date() if effective else (datetime.utcnow() + timedelta(days=1)).date()

#         response = {
#             "success": True,
#             "data": {
#                 "status": "success",
#                 "policyChangeId": str(uuid.uuid4()),
#                 "message": "Policy upgrade request processed successfully.",
#                 "changeType": change_type,
#                 "previousPremium": str(previous_premium),
#                 "newPremium": new_premium,
#                 "effectiveDate": str(effective_date),
#                 "policyChanges": {
#                     "fromPolicy": from_policy,
#                     "toPolicy": to_policy
#                 },
#                 "dependantChanges": dependant_changes,
#                 "timestamp": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
#             },
#             "message": "Operation successful"
#         }

#         return jsonify(response), 201

#     except Exception as e:
#         return jsonify({"success": False, "message": str(e)}), 500


@app.route("/riders/attach", methods=["POST"])
def add_riders():
    try:
        data = request.get_json()

        # Extract request body
        rider_id = data.get("riderId")
        cover_amount = data.get("coverAmount")
        dependants = data.get("dependants", [])

        # Normally you'd fetch these details from DB
        rider_name = "Memorial Service"
        rider_description = "Covers memorial service expenses"

        # Simulate premium calculation (replace with real business logic)
        main_rider_premium = "10.00"
        dependant_rider_premium = "10.00"
        current_premium = "5.50"
        new_premium = 25.5

        # Build response
        response = {
            "success": True,
            "message": "Riders premiums processed successfully",
            "data": {
                "insuranceId": "325cd635-ae3c-414e-84fa-e0da3f1f81ac",
                "attachedRiders": {
                    "mainRider": [
                        {
                            "coverAmount": cover_amount,
                            "riderId": rider_id,
                            "premium": main_rider_premium,
                            "name": rider_name,
                            "description": rider_description
                        }
                    ],
                    "dependants": [
                        {
                            "riderId": dep.get("riderId"),
                            "coverAmount": dep.get("coverAmount"),
                            "premium": dependant_rider_premium,
                            "dependantId": dep.get("dependantId"),
                            "name": rider_name,
                            "description": rider_description
                        }
                        for dep in dependants
                    ]
                },
                "currentPremium": current_premium,
                "newPremium": new_premium
            }
        }

        return jsonify(response), 201

    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500


@app.route("/premiums/payment", methods=["POST"])
def pay_premium():
    try:
        data = request.get_json()

        insurance_id = data.get("insuranceId")
        insurance_type = data.get("insuranceType")
        use_previous_payment_method = data.get("usePreviousPaymentMethod", False)

        payment_details = data.get("paymentDetails", {})
        payment_method = payment_details.get("paymentMethod")
        account_number = payment_details.get("accountNumber")
        months = payment_details.get("months")
        amount = payment_details.get("amount")

        # Simulate payment processing (you can add your logic here)
        result = {
            "status": True,
            "message": f"Payment for {insurance_type} payment successful",
            "data": {
                "insuranceId": insurance_id,
                "insuranceType": insurance_type,
                "usePreviousPaymentMethod": use_previous_payment_method,
                "paymentDetails": {
                    "paymentMethod": payment_method,
                    "accountNumber": account_number,
                    "months": months,
                    "amount": amount,
                }
            }
        }

        return jsonify(result), 201

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


# Configure uploads folder
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/claims/life", methods=["POST"])
def submit_claim():
    try:
        # ✅ Text fields
        insurance_id = request.form.get("insuranceId")
        dependant_id = request.form.get("dependantId")
        phone = request.form.get("phone")
        email = request.form.get("email")
        policy_type = request.form.get("policyType")
        deceased_name = request.form.get("deceasedName")
        deceased_date_of_death = request.form.get("deceasedDateOfDeath")
        cause_of_death = request.form.get("causeOfDeath")
        place_of_death = request.form.get("placeOfDeath")

        # ✅ File uploads
        burial_order_file = request.files.get("burialOrderNumber")
        policy_holder_id_file = request.files.get("policyHolderIdCopy")
        death_certificate_file = request.files.get("deathCertificate")

        proof_of_banking_file = request.files.get("bankDetails[proofOfBanking]")
        affidavit_file = request.files.get("bankDetails[affidavit]")

        # ✅ Bank details (nested keys are sent as form fields)
        account_number = request.form.get("bankDetails[accountNumber]")
        account_type = request.form.get("bankDetails[accountType]")
        account_holder_name = request.form.get("bankDetails[accountHolderName]")
        bank_name = request.form.get("bankDetails[bankName]")

        # Save uploaded files
        saved_files = {}
        for key, file in {
            "burial_order": burial_order_file,
            "policy_holder_id": policy_holder_id_file,
            "death_certificate": death_certificate_file,
            "proof_of_banking": proof_of_banking_file,
            "affidavit": affidavit_file,
        }.items():
            if file:
                filename = secure_filename(file.filename)
                filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
                file.save(filepath)
                saved_files[key] = filepath

        # ✅ Build response
        response = {
            "message": "Claim received successfully",
            "data": {
                "insuranceId": insurance_id,
                "dependantId": dependant_id,
                "phone": phone,
                "email": email,
                "policyType": policy_type,
                "deceasedName": deceased_name,
                "deceasedDateOfDeath": deceased_date_of_death,
                "causeOfDeath": cause_of_death,
                "placeOfDeath": place_of_death,
                "bankDetails": {
                    "accountNumber": account_number,
                    "accountType": account_type,
                    "accountHolderName": account_holder_name,
                    "bankName": bank_name,
                },
                "uploadedFiles": saved_files,
            },
        }

        return jsonify(response), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/dependants/list', methods=['GET'])
def get_dependants():
    return jsonify({"success": True, "data": [
        {
            "id": "55321d5a-f054-4402-9fa0-a3b4c7b1b6bb",
            "userId": "d2f52404-1041-701e-e810-4dc57855f83d",
            "title": "Mr",
            "relationship": "Brother",
            "gender": "male",
            "firstName": "James",
            "lastName": "Murphy",
            "nationalId": "1400009M12",
            "passportNumber": None,
            "dateOfBirth": "1980-06-20T00:00:00.000000Z",
            "phoneNumber": "+263712252252",
            "email": "test@usu.co.zw",
            "province": "Midlands",
            "address": "44 Mainway Meadows",
            "lifeInsurances": [],
            "travelInsurances": []
        },
        {
            "id": "3d22372e-0d73-4d6d-92aa-2c02a5aace5f",
            "userId": "d2f52404-1041-701e-e810-4dc57855f83d",
            "title": "Mrs",
            "relationship": "Wifey",
            "gender": "male",
            "firstName": "Layla",
            "lastName": "Murphy",
            "nationalId": "1500009M12",
            "passportNumber": None,
            "dateOfBirth": "1990-06-20T00:00:00.000000Z",
            "phoneNumber": "+263712252009",
            "email": None,
            "province": "Midlands",
            "address": "44 Mainway Meadows",
            "lifeInsurances": [],
            "travelInsurances": []
        },
        {
            "id": "79e0379f-8699-464e-afc4-652aeb8a328e",
            "userId": "d2f52404-1041-701e-e810-4dc57855f83d",
            "title": "Miss",
            "relationship": "Daughter",
            "gender": "male",
            "firstName": "Elen",
            "lastName": "Murphy",
            "nationalId": "1700009M12",
            "passportNumber": None,
            "dateOfBirth": "2015-06-20T00:00:00.000000Z",
            "phoneNumber": None,
            "email": None,
            "province": "Midlands",
            "address": "44 Mainway Meadows",
            "lifeInsurances": [],
            "travelInsurances": []
        }
    ]})


dependants_store = []


@app.route('/dependants/add', methods=['POST'])
def add_dependants():
    data = request.get_json()
    user_id = data.get('userId')
    dependants = data.get('dependants', [])
    response_data = []

    for dep in dependants:
        dep_id = str(uuid.uuid4())
        date_of_birth = dep.get('dateOfBirth')
        # Format dateOfBirth to "YYYY-MM-DDT00:00:00.000000Z"
        dob_formatted = None
        if date_of_birth:
            try:
                dob_obj = datetime.strptime(date_of_birth, "%Y-%m-%d")
                dob_formatted = dob_obj.strftime(
                    "%Y-%m-%dT00:00:00.000000Z")
            except Exception:
                dob_formatted = date_of_birth  # fallback

        dependant_obj = {
            "id": dep_id,
            "userId": user_id,
            "title": dep.get("title"),
            "relationship": dep.get("relationship"),
            "gender": dep.get("gender"),
            "firstName": dep.get("firstName"),
            "lastName": dep.get("lastName"),
            "nationalId": dep.get("nationalId"),
            "passportNumber": None,
            "dateOfBirth": dob_formatted,
            "phoneNumber": dep.get("phoneNumber") or None,
            "email": dep.get("email") or None,
            "province": dep.get("province"),
            "address": dep.get("address")
        }
        dependants_store.append(dependant_obj)
        response_data.append(dependant_obj)

    return jsonify({"success": True, "data": response_data}), 201

# Get riders


@app.route('/riders/list', methods=['GET'])
def get_riders():
    return jsonify(riders)


subsrcibed_policies = {
    "success": True,
    "data": [
        {
            "id": "7bd37e4a-e16d-46db-ad95-8db0e03a9789",
            "userId": "c2759474-10a1-706e-cbaf-542d48eb1aa6",
            "policyNumber": "45300059",
            "policyRefNumber": "68480243D7FAC",
            "policyType": "FLEX",
            "currency": "USD",
            "premiumAmount": "4.83",
            "funeralPolicyId": None,
            "withBus": False,
            "status": "ACTIVE",
            "activatedAt": "2025-06-10T10:00:35+00:00",
            "expiresAt": "2026-06-10T10:00:35+00:00",
            "failedAt": None,
            "cancelledAt": None,
            "cancellationReason": None,
            "failureReason": None,
            "createdAt": "2025-06-10T09:59:49+00:00",
            "updatedAt": "2025-06-10T10:00:37+00:00"
        },
        {
            "id": "325cd635-ae3c-414e-84fa-e0da3f1f81ac",
            "userId": "c2759474-10a1-706e-cbaf-542d48eb1aa6",
            "policyNumber": "48512651",
            "policyRefNumber": "684801A1F30D8",
            "policyType": "FUNERAL",
            "currency": "USD",
            "premiumAmount": "5.50",
            "funeralPolicyId": None,
            "withBus": False,
            "status": "ACTIVE",
            "activatedAt": "2025-06-10T09:57:53+00:00",
            "expiresAt": "2026-06-10T09:57:53+00:00",
            "failedAt": None,
            "cancelledAt": None,
            "cancellationReason": None,
            "failureReason": None,
            "createdAt": "2025-06-10T09:57:04+00:00",
            "updatedAt": "2025-06-10T14:03:44+00:00"
        }
    ],
    "meta": {
        "count": 2,
        "model_type": "LifeInsurance"
    }
}


riders = {
    "success": True,
    "message": "Riders retrieved successfully",
    "data": [
        {
            "id": "c5b908b8-ccf9-4527-bd5b-dbb873507557",
            "name": None,
            "description": "Provides monthly income stabilization",
            "extra_premium": "25.00",
            "active": True,
            "metadata": {
                "max_amount": 2500,
                "min_amount": 500,
                "max_for_dependents": 1000,
                "applicable_to": "main_member_only"
            },
            "created_at": "2025-06-09T09:32:29.000000Z",
            "updated_at": "2025-06-09T09:32:29.000000Z"
        },
        {
            "id": "a1b908b8-ccf9-4527-bd5b-dbb873507558",
            "name": "Additional Cash",
            "description": "Provides additional cash benefits",
            "extra_premium": "15.00",
            "active": True,
            "metadata": {
                "max_amount": 2500,
                "min_amount": 500,
                "max_for_dependents": 1000
            },
            "created_at": "2025-06-09T09:32:29.000000Z",
            "updated_at": "2025-06-09T09:32:29.000000Z"
        },
        {
            "id": "b2c908b8-ccf9-4527-bd5b-dbb873507559",
            "name": "Memorial Service",
            "description": "Covers memorial service expenses",
            "extra_premium": "10.00",
            "active": True,
            "metadata": {
                "max_for_child_dependent": 500
            },
            "created_at": "2025-06-09T09:32:29.000000Z",
            "updated_at": "2025-06-09T09:32:29.000000Z"
        },
        {
            "id": "d3e908b8-ccf9-4527-bd5b-dbb873507560",
            "name": "Tombstone",
            "description": "Covers tombstone expenses",
            "extra_premium": "10.00",
            "active": True,
            "metadata": {
                "max_for_child_dependent": 500
            },
            "created_at": "2025-06-09T09:32:29.000000Z",
            "updated_at": "2025-06-09T09:32:29.000000Z"
        }
    ]
}

policies = {
    "success": True,
    "data": [
        {
            "id": 1,
            "uuid": "f4b619c7-aea8-4856-bfe7-1164b11dfbbc",
            "policy_name": "Lite",
            "with_bus": False,
            "currency": None,
            "premium": "244444.00",
            "min_payout": "0.00",
            "max_payout": "0.00",
            "status": "active",
            "created_at": "2025-04-14T06:25:28.000000Z",
            "updated_at": "2025-04-14T06:25:28.000000Z"
        },
        {
            "id": 2,
            "uuid": "cde416c0-1319-43e1-9cae-06aa2f025d01",
            "policy_name": "Lite",
            "with_bus": True,
            "currency": "USD",
            "premium": "5.25",
            "min_payout": "0.00",
            "max_payout": "0.00",
            "status": "active",
            "created_at": "2025-04-14T06:25:28.000000Z",
            "updated_at": "2025-04-14T06:25:28.000000Z"
        },
        {
            "id": 3,
            "uuid": "c99c6fd9-34bb-4c8d-91ba-b975975b38fb",
            "policy_name": "Classic",
            "with_bus": False,
            "currency": "USD",
            "premium": "3.25",
            "min_payout": "0.00",
            "max_payout": "0.00",
            "status": "active",
            "created_at": "2025-04-14T06:25:28.000000Z",
            "updated_at": "2025-04-14T06:25:28.000000Z"
        },
        {
            "id": 4,
            "uuid": "67b8b384-cec4-4300-9ef8-f7d103dd5006",
            "policy_name": "Classic",
            "with_bus": True,
            "currency": "USD",
            "premium": None,
            "min_payout": "0.00",
            "max_payout": "0.00",
            "status": "active",
            "created_at": "2025-04-14T06:25:28.000000Z",
            "updated_at": "2025-04-14T06:25:28.000000Z"
        },
        {
            "id": 5,
            "uuid": "38381a4d-3fc4-4720-a115-22310a3aa95a",
            "policy_name": "Premium",
            "with_bus": None,
            "currency": "USD",
            "premium": "10.00",
            "min_payout": "0.00",
            "max_payout": "0.00",
            "status": "active",
            "created_at": "2025-04-14T06:25:28.000000Z",
            "updated_at": "2025-04-14T06:25:28.000000Z"
        },
        {
            "id": 6,
            "uuid": "c403aea2-5ff1-45aa-8466-ba29e062da66",
            "policy_name": "Premium",
            "with_bus": True,
            "currency": "USD",
            "premium": "12.25",
            "min_payout": "0.00",
            "max_payout": "0.00",
            "status": "active",
            "created_at": "2025-04-14T06:25:28.000000Z",
            "updated_at": "2025-04-14T06:25:28.000000Z"
        },
        {
            "id": 7,
            "uuid": "5a6cc8da-a848-4cae-9d11-cc22cf69456e",
            "policy_name": "Supreme",
            "with_bus": False,
            "currency": "USD",
            "premium": "13.25",
            "min_payout": "0.00",
            "max_payout": "0.00",
            "status": "active",
            "created_at": "2025-04-14T06:25:28.000000Z",
            "updated_at": "2025-04-14T06:25:28.000000Z"
        },
        {
            "id": 8,
            "uuid": "c232450c-d4fa-45f9-bb3e-5c18757abf40",
            "policy_name": "Supreme",
            "with_bus": True,
            "currency": "USD",
            "premium": "15.75",
            "min_payout": "0.00",
            "max_payout": "0.00",
            "status": "active",
            "created_at": "2025-04-14T06:25:28.000000Z",
            "updated_at": "2025-04-14T06:25:28.000000Z"
        },
        {
            "id": 9,
            "uuid": "b0c0a6d8-77b5-4757-97b4-2a5b9b532547",
            "policy_name": "Lite",
            "with_bus": False,
            "currency": "ZWG",
            "premium": "16.40",
            "min_payout": "579.58",
            "max_payout": "0.00",
            "status": "active",
            "created_at": "2025-04-14T06:25:28.000000Z",
            "updated_at": "2025-04-14T06:25:28.000000Z"
        },
        {
            "id": 10,
            "uuid": "e854c0b6-8988-4bcc-bace-24d29b4c8c01",
            "policy_name": "Lite",
            "with_bus": True,
            "currency": "ZWG",
            "premium": "30.64",
            "min_payout": "579.58",
            "max_payout": "0.00",
            "status": "active",
            "created_at": "2025-04-14T06:25:28.000000Z",
            "updated_at": "2025-04-14T06:25:28.000000Z"
        },
        {
            "id": 11,
            "uuid": "04da0946-ef04-4797-b30e-6b30c69cbf2e",
            "policy_name": "Classic",
            "with_bus": False,
            "currency": "ZWG",
            "premium": "20.32",
            "min_payout": "1448.95",
            "max_payout": "0.00",
            "status": "active",
            "created_at": "2025-04-14T06:25:28.000000Z",
            "updated_at": "2025-04-14T06:25:28.000000Z"
        },
        {
            "id": 12,
            "uuid": "dae9c049-b07b-4853-8237-a7982e877e3f",
            "policy_name": "Classic",
            "with_bus": True,
            "currency": "ZWG",
            "premium": "34.57",
            "min_payout": "1448.95",
            "max_payout": "0.00",
            "status": "active",
            "created_at": "2025-04-14T06:25:29.000000Z",
            "updated_at": "2025-04-14T06:25:29.000000Z"
        },
        {
            "id": 13,
            "uuid": "f5b63a56-0676-4220-86d9-d7e90d311e29",
            "policy_name": "Premium",
            "with_bus": False,
            "currency": "ZWG",
            "premium": "57.43",
            "min_payout": "4346.85",
            "max_payout": "0.00",
            "status": "active",
            "created_at": "2025-04-14T06:25:29.000000Z",
            "updated_at": "2025-04-14T06:25:29.000000Z"
        },
        {
            "id": 14,
            "uuid": "1060e0d9-def7-4927-97c9-692e2899ea76",
            "policy_name": "Premium",
            "with_bus": True,
            "currency": "ZWG",
            "premium": "71.68",
            "min_payout": "4346.85",
            "max_payout": "0.00",
            "status": "active",
            "created_at": "2025-04-14T06:25:29.000000Z",
            "updated_at": "2025-04-14T06:25:29.000000Z"
        },
        {
            "id": 15,
            "uuid": "723b7eeb-f5d7-4522-b647-d1da4d59ebd2",
            "policy_name": "Supreme",
            "with_bus": False,
            "currency": "ZWG",
            "premium": "76.58",
            "min_payout": "5795.80",
            "max_payout": "0.00",
            "status": "active",
            "created_at": "2025-04-14T06:25:29.000000Z",
            "updated_at": "2025-04-14T06:25:29.000000Z"
        },
        {
            "id": 16,
            "uuid": "9a385c5e-c7d2-4d25-a463-d14049268bd1",
            "policy_name": "Supreme",
            "with_bus": True,
            "currency": "ZWG",
            "premium": "90.83",
            "min_payout": "5795.80",
            "max_payout": "0.00",
            "status": "active",
            "created_at": "2025-04-14T06:25:29.000000Z",
            "updated_at": "2025-04-14T06:25:29.000000Z"
        }
    ]
}

new_flex_policies = {
    "success": True,
    "data": [
        {
            "id": "85adbdd4-3d50-4ced-8b1d-9eaf952ef4f9",
            "policyName": "Lite",
            "withBus": False,
            "currency": "USD",
            "premium": "2.75",
            "minPayout": "0.00",
            "maxPayout": "0.00",
            "status": "active",
            "createdAt": "2025-09-22T06:35:58.000000Z",
            "updatedAt": "2025-09-22T06:35:58.000000Z"
        },
        {
            "id": "195000a3-cd06-4241-865d-0b39c91dafbf",
            "policyName": "Lite",
            "withBus": True,
            "currency": "USD",
            "premium": "5.25",
            "minPayout": "0.00",
            "maxPayout": "0.00",
            "status": "active",
            "createdAt": "2025-09-22T06:35:58.000000Z",
            "updatedAt": "2025-09-22T06:35:58.000000Z"
        },
        {
            "id": "baa9dcc9-1d7f-46a5-a585-7d685977d1a0",
            "policyName": "Classic",
            "withBus": False,
            "currency": "USD",
            "premium": "3.25",
            "minPayout": "0.00",
            "maxPayout": "0.00",
            "status": "active",
            "createdAt": "2025-09-22T06:35:58.000000Z",
            "updatedAt": "2025-09-22T06:35:58.000000Z"
        },
        {
            "id": "3e584bf4-8ea1-430e-8df0-a130815f118c",
            "policyName": "Classic",
            "withBus": True,
            "currency": "USD",
            "premium": "5.50",
            "minPayout": "0.00",
            "maxPayout": "0.00",
            "status": "active",
            "createdAt": "2025-09-22T06:35:58.000000Z",
            "updatedAt": "2025-09-22T06:35:58.000000Z"
        },
        {
            "id": "aa8b63ae-8137-44d7-953c-6b8b479a227d",
            "policyName": "Premium",
            "withBus": False,
            "currency": "USD",
            "premium": "10.00",
            "minPayout": "0.00",
            "maxPayout": "0.00",
            "status": "active",
            "createdAt": "2025-09-22T06:35:58.000000Z",
            "updatedAt": "2025-09-22T06:35:58.000000Z"
        },
        {
            "id": "9334ebac-829f-4cd9-ba94-32c2cfa0788a",
            "policyName": "Premium",
            "withBus": True,
            "currency": "USD",
            "premium": "12.25",
            "minPayout": "0.00",
            "maxPayout": "0.00",
            "status": "active",
            "createdAt": "2025-09-22T06:35:58.000000Z",
            "updatedAt": "2025-09-22T06:35:58.000000Z"
        },
        {
            "id": "56f5ebdf-3b18-436c-9567-f764dfd0ff36",
            "policyName": "Supreme",
            "withBus": False,
            "currency": "USD",
            "premium": "13.25",
            "minPayout": "0.00",
            "maxPayout": "0.00",
            "status": "active",
            "createdAt": "2025-09-22T06:35:58.000000Z",
            "updatedAt": "2025-09-22T06:35:58.000000Z"
        },
        {
            "id": "41bafcc3-3702-45be-953c-4cb4bb9983f2",
            "policyName": "Supreme",
            "withBus": True,
            "currency": "USD",
            "premium": "15.75",
            "minPayout": "0.00",
            "maxPayout": "0.00",
            "status": "active",
            "createdAt": "2025-09-22T06:35:58.000000Z",
            "updatedAt": "2025-09-22T06:35:58.000000Z"
        },
        {
            "id": "71071bd5-04e8-4b17-b987-e3f1d9d17fec",
            "policyName": "Lite",
            "withBus": False,
            "currency": "ZWG",
            "premium": "16.40",
            "minPayout": "579.58",
            "maxPayout": "0.00",
            "status": "active",
            "createdAt": "2025-09-22T06:35:58.000000Z",
            "updatedAt": "2025-09-22T06:35:58.000000Z"
        },
        {
            "id": "4fd8970a-ff49-47b3-8423-d2dd064e9388",
            "policyName": "Lite",
            "withBus": True,
            "currency": "ZWG",
            "premium": "30.64",
            "minPayout": "579.58",
            "maxPayout": "0.00",
            "status": "active",
            "createdAt": "2025-09-22T06:35:58.000000Z",
            "updatedAt": "2025-09-22T06:35:58.000000Z"
        },
        {
            "id": "0d7a1ea1-0129-4e5c-9473-2dd8a5af4aac",
            "policyName": "Classic",
            "withBus": False,
            "currency": "ZWG",
            "premium": "20.32",
            "minPayout": "1448.95",
            "maxPayout": "0.00",
            "status": "active",
            "createdAt": "2025-09-22T06:35:58.000000Z",
            "updatedAt": "2025-09-22T06:35:58.000000Z"
        },
        {
            "id": "7575cb79-c72c-4658-bc69-22428d0c4125",
            "policyName": "Classic",
            "withBus": True,
            "currency": "ZWG",
            "premium": "34.57",
            "minPayout": "1448.95",
            "maxPayout": "0.00",
            "status": "active",
            "createdAt": "2025-09-22T06:35:58.000000Z",
            "updatedAt": "2025-09-22T06:35:58.000000Z"
        },
        {
            "id": "1cb68ac3-7032-43ef-abee-535fee14ad0c",
            "policyName": "Premium",
            "withBus": False,
            "currency": "ZWG",
            "premium": "57.43",
            "minPayout": "4346.85",
            "maxPayout": "0.00",
            "status": "active",
            "createdAt": "2025-09-22T06:35:58.000000Z",
            "updatedAt": "2025-09-22T06:35:58.000000Z"
        },
        {
            "id": "1ea99403-e4cd-41c0-8a44-1072585dd21f",
            "policyName": "Premium",
            "withBus": True,
            "currency": "ZWG",
            "premium": "71.68",
            "minPayout": "4346.85",
            "maxPayout": "0.00",
            "status": "active",
            "createdAt": "2025-09-22T06:35:58.000000Z",
            "updatedAt": "2025-09-22T06:35:58.000000Z"
        },
        {
            "id": "04d71264-9421-4ee6-93a8-b589d8277d69",
            "policyName": "Supreme",
            "withBus": False,
            "currency": "ZWG",
            "premium": "76.58",
            "minPayout": "5795.80",
            "maxPayout": "0.00",
            "status": "active",
            "createdAt": "2025-09-22T06:35:58.000000Z",
            "updatedAt": "2025-09-22T06:35:58.000000Z"
        },
        {
            "id": "4beef4e4-c18a-4fb5-a37a-4b2fbb71b8d1",
            "policyName": "Supreme",
            "withBus": True,
            "currency": "ZWG",
            "premium": "90.83",
            "minPayout": "5795.80",
            "maxPayout": "0.00",
            "status": "active",
            "createdAt": "2025-09-22T06:35:58.000000Z",
            "updatedAt": "2025-09-22T06:35:58.000000Z"
        }
    ]
}

flex_policies = {
    "success": True,
    "data": [
        {
            "id": 1,
            "uuid": "2a833650-96a2-4c0d-95cf-e05e9deb99d3",
            "ageStart": 0,
            "ageEnd": 17,
            "coverMultiple": "0.00",
            "currency": "USD",
            "premium": None,
            "minPayout": "1000.00",
            "maxPayout": "0.00",
            "status": "active",
            "created_at": "2025-04-14T06:25:29.000000Z",
            "updated_at": "2025-04-14T06:25:29.000000Z"
        },
        {
            "id": 2,
            "uuid": "e480ecd7-c0fe-4529-acde-ee7ea3916b71",
            "ageStart": 18,
            "ageEnd": 65,
            "coverMultiple": "0.00",
            "currency": "USD",
            "premium": "1.80",
            "minPayout": "1000.00",
            "maxPayout": "0.00",
            "status": "active",
            "created_at": "2025-04-14T06:25:29.000000Z",
            "updated_at": "2025-04-14T06:25:29.000000Z"
        },
        {
            "id": 3,
            "uuid": "38ba505e-4e06-49f2-9b81-f5edb33f46ed",
            "ageStart": 66,
            "ageEnd": 75,
            "coverMultiple": "0.00",
            "currency": "USD",
            "premium": "5.50",
            "minPayout": "1000.00",
            "maxPayout": "0.00",
            "status": "active",
            "created_at": "2025-04-14T06:25:29.000000Z",
            "updated_at": "2025-04-14T06:25:29.000000Z"
        },
        {
            "id": 4,
            "uuid": "7a74e122-6c8d-4052-bf74-bab8ee54f9da",
            "ageStart": 0,
            "ageEnd": 17,
            "coverMultiple": "1000.00",
            "currency": "ZIG",
            "premium": "1.50",
            "minPayout": "2851.46",
            "maxPayout": "28514.55",
            "status": "active",
            "created_at": "2025-04-14T06:25:29.000000Z",
            "updated_at": "2025-04-14T06:25:29.000000Z"
        },
        {
            "id": 5,
            "uuid": "8bc6b9c5-5dee-4e84-956e-c4628bacf5db",
            "ageStart": 18,
            "ageEnd": 65,
            "coverMultiple": "1000.00",
            "currency": "ZIG",
            "premium": "1.80",
            "minPayout": "2851.46",
            "maxPayout": "28514.55",
            "status": "active",
            "created_at": "2025-04-14T06:25:29.000000Z",
            "updated_at": "2025-04-14T06:25:29.000000Z"
        },
        {
            "id": 6,
            "uuid": "48d40ef0-0e5d-4fb3-8093-e4dab2f090a7",
            "ageStart": 66,
            "ageEnd": 75,
            "coverMultiple": "1000.00",
            "currency": "ZIG",
            "premium": "5.50",
            "minPayout": "2851.46",
            "maxPayout": "11405.82",
            "status": "active",
            "created_at": "2025-04-14T06:25:29.000000Z",
            "updated_at": "2025-04-14T06:25:29.000000Z"
        },
        {
            "id": 7,
            "uuid": "7aaa13b7-d4ca-4ecf-be61-563fd9d260eb",
            "ageStart": 0,
            "ageEnd": 17,
            "coverMultiple": "1000.00",
            "currency": "ZWG",
            "premium": "1.50",
            "minPayout": "2851.46",
            "maxPayout": "28514.55",
            "status": "active",
            "created_at": "2025-04-14T06:25:29.000000Z",
            "updated_at": "2025-04-14T06:25:29.000000Z"
        },
        {
            "id": 8,
            "uuid": "8a88d0da-ddc9-4a19-869a-be2142412296",
            "ageStart": 18,
            "ageEnd": 65,
            "coverMultiple": "1000.00",
            "currency": "ZWG",
            "premium": "1.80",
            "minPayout": "2851.46",
            "maxPayout": "28514.55",
            "status": "active",
            "created_at": "2025-04-14T06:25:29.000000Z",
            "updated_at": "2025-04-14T06:25:29.000000Z"
        },
        {
            "id": 9,
            "uuid": "e58405ef-f15d-4afd-bc7b-dfb55d18b261",
            "ageStart": 66,
            "ageEnd": 75,
            "coverMultiple": "1000.00",
            "currency": "ZWG",
            "premium": "5.50",
            "minPayout": "2851.46",
            "maxPayout": "11405.82",
            "status": "active",
            "created_at": "2025-04-14T06:25:29.000000Z",
            "updated_at": "2025-04-14T06:25:29.000000Z"
        }
    ]
}


if __name__ == '__main__':
    app.run(debug=True)
