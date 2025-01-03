from .API import API
from .utils import make_body, check_address , get_config, get_API_config
import requests
from requests.exceptions import RequestException
import time
import json
import logging

class ProcessLogger:
    def __init__(self, log_file):
        if log_file :
            self.logger = logging.getLogger("ProcessLogger")
            self.logger.setLevel(logging.INFO)
            formatter = logging.Formatter(
                "%(asctime)s | Address: %(address)s | Cause: %(cause)s | Source: %(source)s | Is Auction: %(is_auction)s"
            )
            file_handler = logging.FileHandler(log_file + "/process.log")
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

    def log_failure(self, address, cause, source_name, is_auction):
        extra = {
            "address": address,
            "cause": cause,
            "source": source_name,
            "is_auction": is_auction,
        }
        self.logger.info("Processing failure logged.", extra=extra)


class Data:
    def __init__(
        self,
        full_address: str,
        is_auction: bool,
        source_name: str,
        opening_bid: float = None,
        max_debt: float = None,
        auction_value: float = None,
        auction_date: str = None,
        property_type: str = None,
        link: str = None,
        occupancy: str = None,
        trustee_name: str = None,
        trustee_phone: str = None,
        trustee_sale_number: str = None,
        apn: str = None,
        sold_date: str = None,
        sold_value: float = None,
        final_judgment: float = None,
        plaintiff: str = None,
        attorney_name: str = None,
        attorney_phone: str = None,
        attorney_bar_no: str = None,
        attorney_firm: str = None,
        defendants: str = None,
        sales_status: str = None,
        nos_amount: float = None,
        total_amount_owed: float = None,
        document_name: str = None,
        case_number: str = None,
        case_type: str = None,
        date_of_filing: str = None,
        probate_case_number: str = None,
    ):
        """
        Initialize an AuctionProperty instance with the following attributes:

        full_address: Full address of the property.
        is_auction: Boolean indicating if the property is an auction property.
        source_name: Name of the source where the property information is obtained.
        opening_bid: Opening bid amount for the auction.
        max_debt: maximum amount of debt.
        auction_value: highest bid at the auction.
        auction_date: Date of the auction.
        property_type: Type of the property (e.g., residential, commercial).
        link: Link to the property listing or auction details.
        occupancy: Occupancy status of the property.
        trustee_name: Name of the trustee handling the auction.
        trustee_phone: Phone number of the trustee.
        trustee_sale_number: Sale number associated with the trustee.
        apn: Assessor's Parcel Number (APN) of the property.
        sold_date: Date the property was sold.
        sold_value: Value for which the property was sold.
        final_judgment: Final judgment amount.
        plaintiff: Plaintiff in the case associated with the property.
        attorney_name: Name of the attorney handling the case.
        attorney_phone: Phone number of the attorney.
        attorney_bar_no: Bar number of the attorney.
        attorney_firm: Firm the attorney is associated with.
        defendants: Defendants in the case associated with the property.
        sales_status: Sales status of the property.
        nos_amount: Notice of Sale (NOS) amount.
        total_amount_owed: Total amount owed on the property.
        document_name: Name of the document related to the property.
        case_number: Case number associated with the property.
        case_type: Type of the case (e.g., foreclosure, probate).
        date_of_filing: Date the case was filed.
        probate_case_number: Probate case number (if applicable).
        """
        self.full_address = full_address
        self.is_auction = is_auction
        self.source_name = source_name
        self.opening_bid = opening_bid
        self.max_debt = max_debt
        self.auction_value = auction_value
        self.auction_date = auction_date
        self.property_type = property_type
        self.link = link
        self.occupancy = occupancy
        self.trustee_name = trustee_name
        self.trustee_phone = trustee_phone
        self.trustee_sale_number = trustee_sale_number
        self.apn = apn
        self.sold_date = sold_date
        self.sold_value = sold_value
        self.final_judgment = final_judgment
        self.plaintiff = plaintiff
        self.attorney_name = attorney_name
        self.attorney_phone = attorney_phone
        self.attorney_bar_no = attorney_bar_no
        self.attorney_firm = attorney_firm
        self.defendants = defendants
        self.sales_status = sales_status
        self.nos_amount = nos_amount
        self.total_amount_owed = total_amount_owed
        self.document_name = document_name
        self.case_number = case_number
        self.case_type = case_type
        self.date_of_filing = date_of_filing
        self.probate_case_number = probate_case_number
    
    def validate(self,logger):
        """Validate data types of the attributes."""
        validations = {
            'full_address': str,
            'is_auction': bool,
            'source_name': str,
            'opening_bid': (float, type(None)),
            'max_debt': (float, type(None)),
            'auction_value': (float, type(None)),
            'auction_date': (str, type(None)),
            'property_type': (str, type(None)),
            'link': (str, type(None)),
            'occupancy': (str, type(None)),
            'trustee_name': (str, type(None)),
            'trustee_phone': (str, type(None)),
            'trustee_sale_number': (str, type(None)),
            'apn': (str, type(None)),
            'sold_date': (str, type(None)),
            'sold_value': (float, type(None)),
            'final_judgment': (float, type(None)),
            'plaintiff': (str, type(None)),
            'attorney_name': (str, type(None)),
            'attorney_phone': (str, type(None)),
            'attorney_bar_no': (str, type(None)),
            'attorney_firm': (str, type(None)),
            'defendants': (str, type(None)),
            'sales_status': (str, type(None)),
            'nos_amount': (float, type(None)),
            'total_amount_owed': (float, type(None)),
            'document_name': (str, type(None)),
            'case_number': (str, type(None)),
            'case_type': (str, type(None)),
            'date_of_filing': (str, type(None)),
            'probate_case_number': (str, type(None)),
        }
        
        for attr, expected_type in validations.items():
            value = getattr(self, attr)
            if not isinstance(value, expected_type):
                print(f"{attr} must be of type {expected_type}, got {type(value)} instead.")
                logger.log_failure(
                        self.full_address,
                        f"{attr} must be of type {expected_type}, got {type(value)} instead. (bad data format)",
                        self.source_name,
                        self.is_auction,
                )
                return False 
        return True


class AuthManager:
    def __init__(self, username, password):
        _, base_url , token_time , _ = get_config()
        self.base_url = base_url
        self.token_time = token_time
        self.session = None
        self.access_token = None
        self.refresh_token = None
        self.expiration_time = None
        self.username = username
        self.password = password
        self.is_authenticated()

    def get_new_tokens(self):
        
        token_endpoint = f"{self.base_url}/api/token/"
        try:
            self.session = requests.Session()
            response = self.session.post(
                token_endpoint,
                data={"username": self.username, "password": self.password},
            )
            response.raise_for_status()
            tokens = response.json()
            self.access_token = tokens.get("access")
            self.refresh_token = tokens.get("refresh")
            expires_in = tokens.get("expires_in", float(self.token_time))
            self.expiration_time = time.time() + expires_in
        except RequestException:
            self.session = None
            self.access_token = None
            self.refresh_token = None
            self.expiration_time = None
            raise Exception("Failed to authenticate. Check your credentials.")

    def refresh_access_token(self):
        refresh_token_endpoint = f"{self.base_url}/api/token/refresh/"
        try:
            response = self.session.post(
                refresh_token_endpoint, data={"refresh": self.refresh_token}
            )
            response.raise_for_status()
            self.access_token = response.json().get("access")
            self.refresh_token = response.json().get("refresh")
            self.expiration_time = time.time() + float(self.token_time)
        except RequestException:
            self.access_token = None
            self.expiration_time = None
            raise Exception("Failed to refresh token.")

    def get_authenticated_session(self):
        if not self.session or not self.access_token:
            self.get_new_tokens()

        if time.time() >= self.expiration_time:
            try:
                self.refresh_access_token()
            except Exception:
                print("Refresh token expired. Re-authenticating...")
                self.get_new_tokens()

        return self.session

    def is_authenticated(
        self,
    ):
        session = self.get_authenticated_session()
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json",
        }
        response = session.get(self.base_url + "/api/leads", headers=headers)
        if response.status_code == 401:
            raise ("there is a problem with login , check your username and password")

    def make_authenticated_request(self, url, method="GET", data=None):

        session = self.get_authenticated_session()
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json",
        }

        try:
            if method == "GET":
                response = session.get(url, headers=headers)
            elif method == "POST":
                response = session.post(url, headers=headers, data=data)
            else:
                raise ValueError("Unsupported HTTP method")

            if response.status_code == 401:
                print("Token expired, re-authenticating...")
                self.get_new_tokens()
                session = self.get_authenticated_session()

                if method == "GET":
                    response = session.get(url)
                elif method == "POST":
                    response = session.post(url, data=data)

            response.raise_for_status()
            return response.json()
        except RequestException as e:
            print(f"Request failed: {e}")
            return None


class ProcessLogic:
    def __init__(self, DATA):
        LOG_PATH , _ , _ , _ = get_config()
        self.logger = ProcessLogger(LOG_PATH)
        self.DATA = DATA

    def initial_layer(self):
        if not self.DATA.is_auction:
            if all([self.DATA.auction_value, self.DATA.final_judgment]):
                if self.DATA.auction_value - self.DATA.final_judgment < 40000:
                    self.logger.log_failure(
                        self.DATA.full_address,
                        "Auction value and final judgment difference < 40000 (initial layer)",
                        self.DATA.source_name,
                        self.DATA.is_auction,
                    )
                    return False
            elif all([self.DATA.sold_value, self.DATA.opening_bid]):
                if self.DATA.sold_value - self.DATA.opening_bid < 40000:
                    self.logger.log_failure(
                        self.DATA.full_address,
                        "Sold value and opening bid difference < 40000 (initial layer)",
                        self.DATA.source_name,
                        self.DATA.is_auction,
                    )
                    return False
        return self.DATA

    def zillow_layer(self):
        if self.DATA.is_auction:
            exclude_status = [
                "SOLD",
                "OTHERS",
                "RECENTLY_SOLD",
                "FOR_SALE",
                "ACTIVE",
                "PENDING",
                "FOR_RENT",
            ]
            if self.DATA.zestimate_low:
                if self.DATA.status in exclude_status:
                    self.logger.log_failure(
                        address=self.DATA.address,
                        cause=f"Status {self.DATA.status} is in exclude_status list (zillow layer)",
                        source_name=self.DATA.source_name,
                        is_auction=self.DATA.is_auction,
                    )
                    return False
                if self.DATA.zestimate_low <= 150000:
                    self.logger.log_failure(
                        address=self.DATA.address,
                        cause=f"Zestimate low {self.DATA.zestimate_low} <= 150,000 (zillow layer)",
                        source_name=self.DATA.source_name,
                        is_auction=self.DATA.is_auction,
                    )
                    return False
                if self.DATA.opening_bid:
                    if self.DATA.opening_bid >= 0.50 * self.DATA.zestimate_low:
                        self.logger.log_failure(
                            address=self.DATA.address,
                            cause=f"Opening bid {self.DATA.opening_bid} >= 50% of Zestimate low {self.DATA.zestimate_low} (zillow layer)",
                            source_name=self.DATA.source_name,
                            is_auction=self.DATA.is_auction,
                        )
                        return False
                if self.DATA.total_amount_owed:
                    if self.DATA.total_amount_owed >= 0.50 * self.DATA.zestimate_low:
                        self.logger.log_failure(
                            address=self.DATA.address,
                            cause=f"Total amount owed {self.DATA.total_amount_owed} >= 50% of Zestimate low {self.DATA.zestimate_low} (zillow layer)",
                            source_name=self.DATA.source_name,
                            is_auction=self.DATA.is_auction,
                        )
                        return False
                    if self.DATA.zestimate_low - self.DATA.total_amount_owed < 100000:
                        self.logger.log_failure(
                            address=self.DATA.address,
                            cause=f"Difference between Zestimate low and total amount owed "
                            f"({self.DATA.zestimate_low - self.DATA.total_amount_owed}) < 100,000 (zillow layer)",
                            source_name=self.DATA.source_name,
                            is_auction=self.DATA.is_auction,
                        )
                        return False
        return self.DATA

    def propstream_layer(self):

        if self.DATA.max_debt:
            self.DATA.debt_status = "debt provided in website"

        last_name = self.DATA.owners[0].get("last_name")
        if any(
            k.lower() in last_name.lower()
            for k in [
                "Construction",
                "Bank",
                "Developers",
                "Land",
                "Corporation",
                "Holdings",
            ]
        ):
            self.logger.log_failure(
                address=self.DATA.address,
                cause=f"Excluded due to last name '{last_name}' (propstream layer)",
                source_name=self.DATA.source_name,
                is_auction=self.DATA.is_auction,
            )
            return False
        if any(
            k.lower() in self.DATA.property_type.lower()
            for k in [
                "Vacant",
                "Mobile",
                "Rural Residence",
                "Public School",
                "Farm Land",
            ]
        ):
            self.logger.log_failure(
                address=self.DATA.address,
                cause=f"Excluded due to property type '{self.DATA.property_type}' (propstream layer)",
                source_name=self.DATA.source_name,
                is_auction=self.DATA.is_auction,
            )
            return False

        if self.DATA.is_auction:
            if all([self.DATA.opening_bid, self.DATA.final_judgment]):
                if max(self.DATA.opening_bid, self.DATA.final_judgment) > 1000:
                    self.DATA.max_debt = max(
                        self.DATA.opening_bid, self.DATA.final_judgment
                    )
                    self.DATA.debt_status = (
                        "maximum value of opening bid and final judgement"
                    )
            elif (
                any(
                    [
                        self.DATA.est_remaining_balance,
                        self.DATA.loans[0]["estimatedLoanBalance"],
                    ]
                )
                and not self.DATA.max_debt
            ):
                est_balance = (
                    self.DATA.est_remaining_balance
                    if self.DATA.est_remaining_balance is not None
                    else 0
                )
                loan_balance = (
                    self.DATA.loans[0]["estimatedLoanBalance"]
                    if self.DATA.loans[0]["estimatedLoanBalance"] is not None
                    else 0
                )
                self.DATA.max_debt = max(est_balance, loan_balance)
                self.DATA.debt_status = (
                    "maximum value of est remaining balance and loan 1 balance"
                )

            if all([self.DATA.max_debt, self.DATA.zestimate_low]):
                if self.DATA.max_debt >= 0.50 * self.DATA.zestimate_low:
                    self.logger.log_failure(
                        address=self.DATA.address,
                        cause=f"Max debt {self.DATA.max_debt} >= 50% of Zestimate low {self.DATA.zestimate_low} (propstream layer)",
                        source_name=self.DATA.source_name,
                        is_auction=self.DATA.is_auction,
                    )
                    return False
                if self.DATA.zestimate_low - self.DATA.max_debt <= 100000:
                    self.logger.log_failure(
                        address=self.DATA.address,
                        cause=f"Zestimate low - Max debt <= 100,000 (propstream layer)",
                        source_name=self.DATA.source_name,
                        is_auction=self.DATA.is_auction,
                    )
                    return False
        else:
            if all([self.DATA.sold_value, self.DATA.est_remaining_balance]):
                if self.DATA.sold_value - self.DATA.est_remaining_balance < 40000:
                    self.logger.log_failure(
                        address=self.DATA.address,
                        cause=f"Sold value {self.DATA.sold_value} - Estimated remaining balance {self.DATA.est_remaining_balance} < 40,000 (propstream layer)",
                        source_name=self.DATA.source_name,
                        is_auction=self.DATA.is_auction,
                    )
                    return False

        return self.DATA

    def start(self):
        if not self.DATA.validate(self.logger) :
            return False ,"bad data format"
        
        if not check_address(self.DATA.full_address):
            self.logger.log_failure(
                address=self.DATA.full_address,
                cause=f"Address is not valid",
                source_name=self.DATA.source_name,
                is_auction=self.DATA.is_auction,
            )
            return False, "address is not valid"
        
        initial_filter = self.initial_layer()
        if not initial_filter:
            return False, "removed by initial filters"

        api = API()

        ###########Zillow#############
        print(self.DATA.full_address, ": starting Zillow Batching", sep="")
        zillow_output = api.get_zillow_output(self.DATA.full_address)
        if zillow_output:
            for key, value in zillow_output.items():
                setattr(self.DATA, key, value)
            zillow_filter = self.zillow_layer()
            if not zillow_filter:
                return False, "removed by zillow filters"
        else:
            self.logger.log_failure(
                address=self.DATA.address,
                cause=f"Zillow API output is None",
                source_name=self.DATA.source_name,
                is_auction=self.DATA.is_auction,
            )

        ###########Propstream#############
        print(self.DATA.full_address, ": starting Propstream Batching", sep="")
        propstream_output = api.get_propstream_output(self.DATA.full_address)
        if propstream_output:
            for key, value in propstream_output.items():
                setattr(self.DATA, key, value)
            propstream_filter = self.propstream_layer()
            if not propstream_filter:
                return False, "removed by propstream filters"
        else:
            self.logger.log_failure(
                address=self.DATA.address,
                cause=f"Propstream API output is None",
                source_name=self.DATA.source_name,
                is_auction=self.DATA.is_auction,
            )
            return False, "propstream API output is none"
        ###########Tracers#############
        print(self.DATA.full_address, ": starting Tracers Batching", sep="")
        tracers_output = []
        for owner in self.DATA.owners:
            tracers_output += api.get_tracer_output(
                owner.get("first_name"),
                owner.get("middle_name"),
                owner.get("last_name"),
                self.DATA.address,
                self.DATA.city,
                self.DATA.state,
                self.DATA.zip,
            )
        setattr(self.DATA, "persons", tracers_output)
        return self.DATA, "process is done"


class Lead:
    def __init__(self, session):
        _, base_url ,_ , _ = get_config()
        self.base_url = base_url
        self.auth_session = session

    def insert(self, data):
        url = f"{self.base_url}/api/leads/"
        source_name = data.get("source_name", None)
        is_auction = data.get("is_auction", None)
        queue = Queue()
        queue.starting_process()
        completed_data, status = ProcessLogic(data, source_name, is_auction).start()
        queue.process_is_done()
        if completed_data:
            response = self.auth_session.make_authenticated_request(
                url, method="POST", data=json.dumps(make_body(completed_data))
            )
            print(response)
        else:
            print(status)


class Queue:
    def __init__(self):
        _,_,_,queue_base_url = get_config()
        self.queue_base_url = queue_base_url

    def starting_process(self):
        response = requests.get(f"{self.queue_base_url}/process")
        if response.status_code == 200:
            self.request_id = response.json().get("request_id")
            return True
        return False

    def process_is_done(self):
        response = requests.post(
            f"{self.queue_base_url}/stop", json={"request_id": self.request_id}
        )
        if response.status_code == 200:
            return True
        return False
