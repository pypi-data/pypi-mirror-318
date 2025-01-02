import os
import json
import usaddress


def check_address(address):
    parsed_address = usaddress.tag(address)[0]
    check = all(
        [
            parsed_address.get("AddressNumber", None),
            parsed_address.get("StreetName", None),
            parsed_address.get("StateName", None),
            parsed_address.get("ZipCode", None),
        ]
    )
    if not check:
        return None
    else:
        return address


def reformat_address(address):
    try:
        parsed_address = usaddress.tag(address)[0]
        occupancy_identifier = ""
        street_name_post_type = ""
        if parsed_address.get("OccupancyIdentifier"):
            occupancy_identifier = f"#{parsed_address.get('OccupancyIdentifier','')},"
        else:
            street_name_post_type = f"{parsed_address.get('StreetNamePostType','')},"

        formatted_address = " ".join(
            [
                parsed_address.get("AddressNumber", ""),
                parsed_address.get("StreetName", ""),
                street_name_post_type,
                occupancy_identifier,
                parsed_address.get("StateName", ""),
                parsed_address.get("ZipCode", ""),
            ]
        )
        formatted_address = " ".join(formatted_address.split())
        return ", ".join(i.strip() for i in formatted_address.split(","))

    except:
        return None


def save_configs(env_path, log_path):
    env_path = env_path.strip()
    if env_path and os.path.exists(env_path) and log_path and os.path.exists(log_path):
        config = {"env_file_path": env_path, "log_file_path": log_path}
        with open("config.json", "w") as f:
            json.dump(config, f)
        print(f"Saved .env file path and log file path to config.json: {env_path}")
        print(f"Saved .log file path to config.json: {log_path}")
    else:
        raise Exception("Error: Invalid path entered.")


def make_obj(row, columns):
    return {key: row[key] if key in row else None for key in columns}


def check_empty_obj(obj):
    return sum(1 for value in obj.values() if value in (None, 0)) != len(obj)


def make_body(row):
    body = {}

    row = {key.lower().replace(" ", "_"): value for key, value in row.items()}
    row = {key: None if value != value else value for key, value in row.items()}

    columns = ["reformatted_address", "source_name", "is_auction"]
    body.update({"duplicate_check": make_obj(row, columns)})

    columns = [
        "address",
        "county",
        "apn",
        "property_type",
        "lot_size",
        "year_built",
        "occupancy_status",
        "bedroom",
        "bathrooms",
        "zestimate",
        "equity",
        "square_footage",
        "zillow_link",
        "status",
    ]
    body.update({"property": make_obj(row, columns)})

    columns = [
        "first_name",
        "last_name",
        "dob",
        "dod",
        "mailing_address",
        "mailing_city",
        "mailing_state",
        "mailing_zip",
    ]
    owner_obj = make_obj(row, columns)
    if check_empty_obj(owner_obj):
        body.update({"owner": owner_obj})

    columns = [
        "auction_date",
        "estimated_resale_value",
        "opening_bid",
        "estimated_debt",
        "rental_estimate",
        "trustee_sale_number",
        "link",
    ]
    auction_obj = make_obj(row, columns)
    if check_empty_obj(auction_obj):
        body.update({"auction": auction_obj})

    columns = ["sale_date", "sold_amount", "sale_status"]
    salesinfo_obj = make_obj(row, columns)
    if check_empty_obj(salesinfo_obj):
        body.update({"salesInformation": salesinfo_obj})

    columns = [
        "document_name",
        "case_type",
        "total_amount_owed",
        "date_of_filing",
        "plaintiff",
        "plaintiff_attorney_firm",
        "plaintiff_attorney_name",
        "plaintiff_atty_bar_no",
        "defendants",
        "probate_case_number",
    ]
    legalproceeding_obj = make_obj(row, columns)
    if check_empty_obj(legalproceeding_obj):
        body.update({"legalproceeding": legalproceeding_obj})

    columns = [
        "loan_type",
        "interest_rate",
        "lender_name",
        "mortgage_date",
        "mortgage_amount",
        "debt",
    ]
    debtmortgage_obj = make_obj(row, columns)
    if check_empty_obj(debtmortgage_obj):
        body.update({"mortgageanddebt": debtmortgage_obj})

    columns = ["lien_type", "lien_date", "lien_amount", "certificate_of_release"]
    taxlien_obj = make_obj(row, columns)
    if check_empty_obj(taxlien_obj):
        body.update({"taxlien": taxlien_obj})

    connection_obj = []
    for i in range(1, 3):
        addr = row.get(f"associate_{i}_address")
        if addr:
            connection_obj.append(
                {
                    "connection_type": "Associate",
                    "name": row[f"associate_{i}_name"],
                    "address": addr,
                    "phone": row[f"associate_{i}_phone"],
                }
            )

    for j in range(1, 3):
        for i in range(1, 4):
            addr = row.get(f"address_{j}_neighbor_{i}_address")
            if addr:
                connection_obj.append(
                    {
                        "connection_type": "Neighbor",
                        "name": row[f"address_{j}_neighbor_{i}_name"],
                        "address": addr,
                        "phone": row[f"address_{j}_neighbor_{i}_phone"],
                    }
                )

    for i in range(1, 11):
        addr = row.get(f"relative_{i}_address")
        if addr:
            connection_obj.append(
                {
                    "connection_type": "Relative",
                    "name": row[f"relative_{i}_name"],
                    "address": addr,
                    "phone": row[f"relative_{i}_phone"],
                }
            )

    body.update({"connections": connection_obj})

    emails_obj = []
    for i in range(1, 4):
        email = row.get(f"email_{i}")
        if email:
            emails_obj.append({"email_address": email})
    body.update({"emails": emails_obj})

    phones_obj = []
    for i in range(1, 4):
        phone = row.get(f"phone_{i}")
        if phone:
            phones_obj.append(
                {
                    "phone_type": row[f"phone_{i}_type"],
                    "phone_connected": bool(row[f"phone_{i}_is_connected"]),
                    "phone_number": phone,
                }
            )
    body.update({"phones": phones_obj})
    return body
