from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/policies', methods=['GET'])
def get_policy():
    return jsonify(policies)


@app.route('/flex-policies', methods=['GET'])
def get_flex_policy():
    return jsonify(flex_policies)


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
