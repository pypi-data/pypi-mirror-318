import requests
from .utils import reformat_address , get_API_config

class API :
    def __init__(self):
        (self.zillow_base_url , self.zillow_username , self.zillow_password,
        self.propstream_base_url , self.propstream_username ,
        self.propstream_password , self.propstream_login_url,
        self.tracers_base_url , self.tracers_username,
        self.tracers_password) = get_API_config()

    def get_zillow_output(self,address):
        url = f"{self.zillow_base_url}?address={address}"

        headers = {
            "X-RapidAPI-Host": self.zillow_username,
            "X-RapidAPI-Key": self.zillow_password
        }
        
        response = requests.get(url, headers=headers)
        try :
            data = response.json()
            status = data.get("homeStatus", None)
            broker = data.get("brokerageName" , None)
            price = data.get("price", 0)
            zestimate = data.get("zestimate", 0)
            zestimateLowPercent = data.get("zestimateLowPercent") if data.get("zestimateLowPercent") else 0
            url = data.get("url")
            if zestimate == None or zestimate == 0 :
                zestimate = price
            if broker == "Auction.com" :
                status = "Auction"
            return {
                        "zestimate": zestimate,
                        "bedrooms": data.get("bedrooms", 0),
                        "bathrooms": data.get("bathrooms", 0),
                        "status": status,
                        "living_area": data.get("livingAreaValue", 0),
                        "zillow_link" : "https://www.zillow.com" + str(url) if url else None,
                        "zestimate_low": zestimate*(100-int(zestimateLowPercent))/100 
        }
        except Exception:
            return None
        

    def get_propstream_output(self,address):
        try :
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
                'Referer': 'https://login.propstream.com/'
            }
            

            s = requests.session()
            s.headers = headers
            login_result = s.post(url=self.propstream_login_url, params={"username" : self.propstream_username,"password":self.propstream_password})
            authToken = s.get(url=f"{self.propstream_base_url}eqbackend/resource/auth?t={login_result.url.split('=')[1]}").json().get("authToken")
            s.headers["X-Auth-Token"] = authToken
            
            formatted_address = reformat_address(address)
            suggest = s.get(f"{self.propstream_base_url}eqbackend/resource/auth/ps4/property/suggestionsnew?q={formatted_address}").json()
            property_id = suggest[0].get("id")
            address_type = suggest[0].get("type")
            result = s.get(f'{self.propstream_base_url}eqbackend/resource/auth/ps4/property?id={property_id}&addressType={address_type}').json()
            s.get(f'{self.propstream_base_url}/logout')

            json_array = result["properties"][0]
            owners = [
                {
                "first_name": json_array.get("owner1FirstName", None),
                "middle_name": json_array.get("owner1MiddleName", None),
                "last_name": json_array.get("owner1LastName", None),
                },
                {
                "first_name": json_array.get("owner2FirstName", None),
                "middle_name": json_array.get("owner2MiddleName", None),
                "last_name": json_array.get("owner2LastName", None),   
                }
            ]

            property_data = {
                "address": json_array["address"].get("streetAddress", None),
                "unit": json_array["address"].get("unitNumber", None),
                "city": json_array["address"].get("cityName", None),
                "state": json_array["address"].get("stateCode", None),
                "zip": json_array["address"].get("zip", None),
                "county": json_array["address"].get("countyName", None),
                "mailing": json_array.get("mailAddress",None),
                "apn": json_array.get("apn", None),
                "owner_occupied": json_array.get("ownerOccupied", None),
                "decedent" : json_array.get("decedent", None),
                "occupancy" : json_array.get("ownerProperty",{}).get("vacant", None),
                "property_type" : json_array.get("landUse", None),
                "owners" : owners ,
                "loans": json_array.get("activeLoans", []),
                "liens":json_array.get("liens", []),
                "foreclosures": json_array.get("foreclosure", []),
                "mortgages": json_array.get("mortgages", []),
                "est_remaining_balance": json_array.get("openMortgageBalance", 0),
            }
            
            return property_data
        except :
            return None


    def person_search(self,payload):
        url = self.tracers_base_url
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "galaxy-ap-name": self.tracers_username,
            "galaxy-ap-password": self.tracers_password,
            "galaxy-search-type": "BackgroundReport"
        }
        response = requests.post(url, json=payload, headers=headers)
        return response.json()

    def get_tracer_output(self,first_name , middle_name , last_name , address , city , state , zip) :
        payload = {
            "firstName": first_name if first_name == first_name else "",
            "middleName": middle_name if middle_name == middle_name else "",
            "lastName": last_name if last_name == last_name else "",
            "Addresses" : [{
                "AddressLine1" : address,
                "AddressLine2" : f"{state} {zip}"
            }]
        }
        data = self.person_search(payload)["persons"]
        persons = []
        for person in data :
            persons.append({
                "first_name" : person["name"]["firstName"],
                "middle_name" : person["name"]["middleName"],
                "last_name" : person["name"]["lastName"],
                "dob" : person.get("dob", None),
                "age" : person.get("age", None),
                "dod" : person.get("dod", None),
                "addresses" : person.get("addresses", []),
                "associates" : person.get("associates",[]),
                "relatives" : person.get("relatives",[]),
                "emails" : person.get("emailAddress",[]),
                "phones" : person.get("phoneNumbers",[])
                })
            
        return persons