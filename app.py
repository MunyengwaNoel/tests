from flask import Flask, jsonify
from flask import request
import uuid
from datetime import datetime

app = Flask(__name__)


@app.route('/policies/subscribed', methods=['GET'])
def get_subscribed_policies():
    return jsonify(subsrcibed_policies)


@app.route('/policies', methods=['GET'])
def get_policy():
    return jsonify(policies)


@app.route('/flex-policies', methods=['GET'])
def get_flex_policy():
    return jsonify(flex_policies)


@app.route('/dependants', methods=['GET'])
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
            "email": None,
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


@app.route('/dependants', methods=['POST'])
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


@app.route('/riders', methods=['GET'])
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
            "name": "Income Stabilisation",
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
            "currency": "USD",
            "premium": "2.75",
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
            "premium": "5.50",
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
            "with_bus": False,
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
            "premium": "1.50",
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
