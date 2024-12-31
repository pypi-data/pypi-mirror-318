import requests

class Ercaspay:
    def __init__(self, ercaspay_secret_key: str) -> None:
        self.sk = ercaspay_secret_key
        self.base_url = "https://api.ercaspay.com/api/v1"
        return None

    def naira_initiate_transaction(self,
                                   amount:float, payment_reference:str,
                                   customer_name:str, customer_email:str,
                                   customer_phone:str = None, redirect_url:str=None,
                                   descrption:str = None) -> dict:
        """
        Initiates a payment transaction with the specified details.

        Parameters:
        amount (float): The amount to be charged for the transaction.
        payment_reference (str): A unique reference for the payment transaction.
        customer_name (str): The name of the customer making the payment.
        customer_email (str): The email address of the customer.
        customer_phone (str, optional): The phone number of the customer. Defaults to None.
        redirect_url (str, optional): The URL to redirect the customer after payment. Defaults to None.
        descrption (str, optional): A description of the transaction. Defaults to None.
        """
        
        url = f"{self.base_url}/payment/initiate"

        headers = {
            "Authorization": f"Bearer {self.sk}",
            "Content-Type": "application/json"
        }

        json_body = {
            "amount": amount, # mandatory parameter
            "paymentReference": payment_reference, # mandatory parameter
            "paymentMethods": "bank-transfer,ussd,card,qrcode", #optional parameter default to those on your dashboard
            "customerName": customer_name, # mandatory parameter
            "customerEmail": customer_email, # mandatory parameter
            "customerPhoneNumber": customer_phone, # optional parameter,
            "redirectUrl": redirect_url, # optional parameter
            "description": descrption, # optional parameter
            "currency": "NGN",
            # "feeBearer": "customer", # optional parameter
            # "metadata": { # optional parameter
            #     "firstname": 
            #     "lastname": 
            #     "email": 
            # }
        }

        post_request = requests.post(url, headers=headers, json=json_body)
        response = post_request.json()
        if post_request.status_code in [200, 201]:  ## Successful request
            output = {
                "tx_status": response["requestSuccessful"],
                "tx_code": response["responseCode"],
                "tx_body": {
                    "payment_reference": response["responseBody"]["paymentReference"],
                    "tx_reference": response["responseBody"]["transactionReference"],
                    "checkoutUrl": response["responseBody"]["checkoutUrl"]
                }
            }

            return output
        ## If not successful
        output = {
                "tx_status": response["requestSuccessful"],
                "tx_code": response["responseCode"],
                "error_message": response['errorMessage'],
                "tx_body": response['responseBody']
                }
        
        return output
    
    ## Initiating US dollars Transaction
    def usd_initiate_transaction(self,
                                 amount:float, payment_reference:str,
                                 customer_name:str, customer_email:str,
                                 customer_phone:str = None, redirect_url:str=None,
                                 descrption:str = None) -> dict:
        """
        Initiates a payment transaction with the specified details.

        Parameters:
        amount (float): The amount to be charged for the transaction.
        payment_reference (str): A unique reference for the payment transaction.
        customer_name (str): The name of the customer making the payment.
        customer_email (str): The email address of the customer.
        customer_phone (str, optional): The phone number of the customer. Defaults to None.
        redirect_url (str, optional): The URL to redirect the customer after payment. Defaults to None.
        descrption (str, optional): A description of the transaction. Defaults to None.
        """
        
        url = f"{self.base_url}/payment/initiate"

        headers = {
            "Authorization": f"Bearer {self.sk}",
            "Content-Type": "application/json"
        }

        json_body = {
            "amount": amount, # mandatory parameter
            "paymentReference": payment_reference, # mandatory parameter
            "paymentMethods": "bank-transfer,ussd,card,qrcode", #optional parameter default to those on your dashboard
            "customerName": customer_name, # mandatory parameter
            "customerEmail": customer_email, # mandatory parameter
            "customerPhoneNumber": customer_phone, # optional parameter,
            "redirectUrl": redirect_url, # optional parameter
            "description": descrption, # optional parameter
            "currency": "USD",
            # "feeBearer": "customer", # optional parameter
            # "metadata": { # optional parameter
            #     "firstname": 
            #     "lastname": 
            #     "email": 
            # }
        }

        post_request = requests.post(url, headers=headers, json=json_body)
        response = post_request.json()
        if post_request.status_code in [200, 201]:  ## Successful request
            output = {
                "tx_status": response["requestSuccessful"],
                "tx_code": response["responseCode"],
                "tx_body": {
                    "payment_reference": response["responseBody"]["paymentReference"],
                    "tx_reference": response["responseBody"]["transactionReference"],
                    "checkoutUrl": response["responseBody"]["checkoutUrl"]
                }
            }

            return output
        ## If not successful
        output = {
                "tx_status": response["requestSuccessful"],
                "tx_code": response["responseCode"],
                "error_message": response['errorMessage'],
                "tx_body": response['responseBody']
                }
        
        return output
       

    def verify_transaction(self, transaction_ref: str) -> dict:
        """
        Verifies a transaction using the provided transaction reference.

        Parameters:
        transaction_ref (str): The unique reference of the transaction to be verified.

        Returns:
        bool: True if the transaction is successfully verified, False otherwise.
        """
        url = f"{self.base_url}/payment/transaction/verify/{transaction_ref}"

        headers = {
            "Authorization": f"Bearer {self.sk}",
            "Content-Type": "application/json"
            }

        get_request = requests.get(url, headers=headers)
        response = get_request.json()

        if get_request.status_code in [200, 201]: ## Successful request
            output = {
                "tx_status": response['requestSuccessful'],
                "tx_code": response["responseCode"],
                "tx_message": response["responseMessage"],
                "tx_body": response["responseBody"]
            }

            return output
        ## if not Verified
        output = {
                "tx_status": response['requestSuccessful'],
                "error_message": response['errorMessage'],
                "tx_code": response["responseCode"],
                "tx_body": response["responseBody"]
            }
        return output
