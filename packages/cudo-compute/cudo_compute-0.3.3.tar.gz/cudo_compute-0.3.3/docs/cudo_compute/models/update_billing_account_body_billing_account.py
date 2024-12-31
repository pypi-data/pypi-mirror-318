# coding: utf-8

"""
    Cudo Compute service

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from src.cudo_compute.configuration import Configuration


class UpdateBillingAccountBodyBillingAccount(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'create_time': 'datetime',
        'display_name': 'str',
        'stripe_ref': 'str',
        'create_by': 'str',
        'monthly_spend': 'str',
        'hourly_spend_rate': 'Decimal',
        'tax_id': 'TaxId',
        'invoice_time': 'datetime',
        'billing_threshold': 'Decimal',
        'monthly_spend_limit': 'Decimal',
        'hourly_spend_limit': 'Decimal',
        'next_invoice_total': 'Decimal',
        'credit_balance': 'Decimal',
        'credit_balance_recharge': 'CreditBalanceRecharge',
        'billing_address': 'BillingAddress',
        'state': 'BillingAccountState',
        'payment_terms': 'PaymentTerms'
    }

    attribute_map = {
        'create_time': 'createTime',
        'display_name': 'displayName',
        'stripe_ref': 'stripeRef',
        'create_by': 'createBy',
        'monthly_spend': 'monthlySpend',
        'hourly_spend_rate': 'hourlySpendRate',
        'tax_id': 'taxId',
        'invoice_time': 'invoiceTime',
        'billing_threshold': 'billingThreshold',
        'monthly_spend_limit': 'monthlySpendLimit',
        'hourly_spend_limit': 'hourlySpendLimit',
        'next_invoice_total': 'nextInvoiceTotal',
        'credit_balance': 'creditBalance',
        'credit_balance_recharge': 'creditBalanceRecharge',
        'billing_address': 'billingAddress',
        'state': 'state',
        'payment_terms': 'paymentTerms'
    }

    def __init__(self, create_time=None, display_name=None, stripe_ref=None, create_by=None, monthly_spend=None, hourly_spend_rate=None, tax_id=None, invoice_time=None, billing_threshold=None, monthly_spend_limit=None, hourly_spend_limit=None, next_invoice_total=None, credit_balance=None, credit_balance_recharge=None, billing_address=None, state=None, payment_terms=None, _configuration=None):  # noqa: E501
        """UpdateBillingAccountBodyBillingAccount - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._create_time = None
        self._display_name = None
        self._stripe_ref = None
        self._create_by = None
        self._monthly_spend = None
        self._hourly_spend_rate = None
        self._tax_id = None
        self._invoice_time = None
        self._billing_threshold = None
        self._monthly_spend_limit = None
        self._hourly_spend_limit = None
        self._next_invoice_total = None
        self._credit_balance = None
        self._credit_balance_recharge = None
        self._billing_address = None
        self._state = None
        self._payment_terms = None
        self.discriminator = None

        if create_time is not None:
            self.create_time = create_time
        if display_name is not None:
            self.display_name = display_name
        if stripe_ref is not None:
            self.stripe_ref = stripe_ref
        if create_by is not None:
            self.create_by = create_by
        if monthly_spend is not None:
            self.monthly_spend = monthly_spend
        if hourly_spend_rate is not None:
            self.hourly_spend_rate = hourly_spend_rate
        if tax_id is not None:
            self.tax_id = tax_id
        if invoice_time is not None:
            self.invoice_time = invoice_time
        if billing_threshold is not None:
            self.billing_threshold = billing_threshold
        if monthly_spend_limit is not None:
            self.monthly_spend_limit = monthly_spend_limit
        if hourly_spend_limit is not None:
            self.hourly_spend_limit = hourly_spend_limit
        if next_invoice_total is not None:
            self.next_invoice_total = next_invoice_total
        if credit_balance is not None:
            self.credit_balance = credit_balance
        if credit_balance_recharge is not None:
            self.credit_balance_recharge = credit_balance_recharge
        if billing_address is not None:
            self.billing_address = billing_address
        if state is not None:
            self.state = state
        if payment_terms is not None:
            self.payment_terms = payment_terms

    @property
    def create_time(self):
        """Gets the create_time of this UpdateBillingAccountBodyBillingAccount.  # noqa: E501


        :return: The create_time of this UpdateBillingAccountBodyBillingAccount.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this UpdateBillingAccountBodyBillingAccount.


        :param create_time: The create_time of this UpdateBillingAccountBodyBillingAccount.  # noqa: E501
        :type: datetime
        """

        self._create_time = create_time

    @property
    def display_name(self):
        """Gets the display_name of this UpdateBillingAccountBodyBillingAccount.  # noqa: E501


        :return: The display_name of this UpdateBillingAccountBodyBillingAccount.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this UpdateBillingAccountBodyBillingAccount.


        :param display_name: The display_name of this UpdateBillingAccountBodyBillingAccount.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def stripe_ref(self):
        """Gets the stripe_ref of this UpdateBillingAccountBodyBillingAccount.  # noqa: E501


        :return: The stripe_ref of this UpdateBillingAccountBodyBillingAccount.  # noqa: E501
        :rtype: str
        """
        return self._stripe_ref

    @stripe_ref.setter
    def stripe_ref(self, stripe_ref):
        """Sets the stripe_ref of this UpdateBillingAccountBodyBillingAccount.


        :param stripe_ref: The stripe_ref of this UpdateBillingAccountBodyBillingAccount.  # noqa: E501
        :type: str
        """

        self._stripe_ref = stripe_ref

    @property
    def create_by(self):
        """Gets the create_by of this UpdateBillingAccountBodyBillingAccount.  # noqa: E501


        :return: The create_by of this UpdateBillingAccountBodyBillingAccount.  # noqa: E501
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        """Sets the create_by of this UpdateBillingAccountBodyBillingAccount.


        :param create_by: The create_by of this UpdateBillingAccountBodyBillingAccount.  # noqa: E501
        :type: str
        """

        self._create_by = create_by

    @property
    def monthly_spend(self):
        """Gets the monthly_spend of this UpdateBillingAccountBodyBillingAccount.  # noqa: E501


        :return: The monthly_spend of this UpdateBillingAccountBodyBillingAccount.  # noqa: E501
        :rtype: str
        """
        return self._monthly_spend

    @monthly_spend.setter
    def monthly_spend(self, monthly_spend):
        """Sets the monthly_spend of this UpdateBillingAccountBodyBillingAccount.


        :param monthly_spend: The monthly_spend of this UpdateBillingAccountBodyBillingAccount.  # noqa: E501
        :type: str
        """

        self._monthly_spend = monthly_spend

    @property
    def hourly_spend_rate(self):
        """Gets the hourly_spend_rate of this UpdateBillingAccountBodyBillingAccount.  # noqa: E501


        :return: The hourly_spend_rate of this UpdateBillingAccountBodyBillingAccount.  # noqa: E501
        :rtype: Decimal
        """
        return self._hourly_spend_rate

    @hourly_spend_rate.setter
    def hourly_spend_rate(self, hourly_spend_rate):
        """Sets the hourly_spend_rate of this UpdateBillingAccountBodyBillingAccount.


        :param hourly_spend_rate: The hourly_spend_rate of this UpdateBillingAccountBodyBillingAccount.  # noqa: E501
        :type: Decimal
        """

        self._hourly_spend_rate = hourly_spend_rate

    @property
    def tax_id(self):
        """Gets the tax_id of this UpdateBillingAccountBodyBillingAccount.  # noqa: E501


        :return: The tax_id of this UpdateBillingAccountBodyBillingAccount.  # noqa: E501
        :rtype: TaxId
        """
        return self._tax_id

    @tax_id.setter
    def tax_id(self, tax_id):
        """Sets the tax_id of this UpdateBillingAccountBodyBillingAccount.


        :param tax_id: The tax_id of this UpdateBillingAccountBodyBillingAccount.  # noqa: E501
        :type: TaxId
        """

        self._tax_id = tax_id

    @property
    def invoice_time(self):
        """Gets the invoice_time of this UpdateBillingAccountBodyBillingAccount.  # noqa: E501


        :return: The invoice_time of this UpdateBillingAccountBodyBillingAccount.  # noqa: E501
        :rtype: datetime
        """
        return self._invoice_time

    @invoice_time.setter
    def invoice_time(self, invoice_time):
        """Sets the invoice_time of this UpdateBillingAccountBodyBillingAccount.


        :param invoice_time: The invoice_time of this UpdateBillingAccountBodyBillingAccount.  # noqa: E501
        :type: datetime
        """

        self._invoice_time = invoice_time

    @property
    def billing_threshold(self):
        """Gets the billing_threshold of this UpdateBillingAccountBodyBillingAccount.  # noqa: E501


        :return: The billing_threshold of this UpdateBillingAccountBodyBillingAccount.  # noqa: E501
        :rtype: Decimal
        """
        return self._billing_threshold

    @billing_threshold.setter
    def billing_threshold(self, billing_threshold):
        """Sets the billing_threshold of this UpdateBillingAccountBodyBillingAccount.


        :param billing_threshold: The billing_threshold of this UpdateBillingAccountBodyBillingAccount.  # noqa: E501
        :type: Decimal
        """

        self._billing_threshold = billing_threshold

    @property
    def monthly_spend_limit(self):
        """Gets the monthly_spend_limit of this UpdateBillingAccountBodyBillingAccount.  # noqa: E501


        :return: The monthly_spend_limit of this UpdateBillingAccountBodyBillingAccount.  # noqa: E501
        :rtype: Decimal
        """
        return self._monthly_spend_limit

    @monthly_spend_limit.setter
    def monthly_spend_limit(self, monthly_spend_limit):
        """Sets the monthly_spend_limit of this UpdateBillingAccountBodyBillingAccount.


        :param monthly_spend_limit: The monthly_spend_limit of this UpdateBillingAccountBodyBillingAccount.  # noqa: E501
        :type: Decimal
        """

        self._monthly_spend_limit = monthly_spend_limit

    @property
    def hourly_spend_limit(self):
        """Gets the hourly_spend_limit of this UpdateBillingAccountBodyBillingAccount.  # noqa: E501


        :return: The hourly_spend_limit of this UpdateBillingAccountBodyBillingAccount.  # noqa: E501
        :rtype: Decimal
        """
        return self._hourly_spend_limit

    @hourly_spend_limit.setter
    def hourly_spend_limit(self, hourly_spend_limit):
        """Sets the hourly_spend_limit of this UpdateBillingAccountBodyBillingAccount.


        :param hourly_spend_limit: The hourly_spend_limit of this UpdateBillingAccountBodyBillingAccount.  # noqa: E501
        :type: Decimal
        """

        self._hourly_spend_limit = hourly_spend_limit

    @property
    def next_invoice_total(self):
        """Gets the next_invoice_total of this UpdateBillingAccountBodyBillingAccount.  # noqa: E501


        :return: The next_invoice_total of this UpdateBillingAccountBodyBillingAccount.  # noqa: E501
        :rtype: Decimal
        """
        return self._next_invoice_total

    @next_invoice_total.setter
    def next_invoice_total(self, next_invoice_total):
        """Sets the next_invoice_total of this UpdateBillingAccountBodyBillingAccount.


        :param next_invoice_total: The next_invoice_total of this UpdateBillingAccountBodyBillingAccount.  # noqa: E501
        :type: Decimal
        """

        self._next_invoice_total = next_invoice_total

    @property
    def credit_balance(self):
        """Gets the credit_balance of this UpdateBillingAccountBodyBillingAccount.  # noqa: E501


        :return: The credit_balance of this UpdateBillingAccountBodyBillingAccount.  # noqa: E501
        :rtype: Decimal
        """
        return self._credit_balance

    @credit_balance.setter
    def credit_balance(self, credit_balance):
        """Sets the credit_balance of this UpdateBillingAccountBodyBillingAccount.


        :param credit_balance: The credit_balance of this UpdateBillingAccountBodyBillingAccount.  # noqa: E501
        :type: Decimal
        """

        self._credit_balance = credit_balance

    @property
    def credit_balance_recharge(self):
        """Gets the credit_balance_recharge of this UpdateBillingAccountBodyBillingAccount.  # noqa: E501


        :return: The credit_balance_recharge of this UpdateBillingAccountBodyBillingAccount.  # noqa: E501
        :rtype: CreditBalanceRecharge
        """
        return self._credit_balance_recharge

    @credit_balance_recharge.setter
    def credit_balance_recharge(self, credit_balance_recharge):
        """Sets the credit_balance_recharge of this UpdateBillingAccountBodyBillingAccount.


        :param credit_balance_recharge: The credit_balance_recharge of this UpdateBillingAccountBodyBillingAccount.  # noqa: E501
        :type: CreditBalanceRecharge
        """

        self._credit_balance_recharge = credit_balance_recharge

    @property
    def billing_address(self):
        """Gets the billing_address of this UpdateBillingAccountBodyBillingAccount.  # noqa: E501


        :return: The billing_address of this UpdateBillingAccountBodyBillingAccount.  # noqa: E501
        :rtype: BillingAddress
        """
        return self._billing_address

    @billing_address.setter
    def billing_address(self, billing_address):
        """Sets the billing_address of this UpdateBillingAccountBodyBillingAccount.


        :param billing_address: The billing_address of this UpdateBillingAccountBodyBillingAccount.  # noqa: E501
        :type: BillingAddress
        """

        self._billing_address = billing_address

    @property
    def state(self):
        """Gets the state of this UpdateBillingAccountBodyBillingAccount.  # noqa: E501


        :return: The state of this UpdateBillingAccountBodyBillingAccount.  # noqa: E501
        :rtype: BillingAccountState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this UpdateBillingAccountBodyBillingAccount.


        :param state: The state of this UpdateBillingAccountBodyBillingAccount.  # noqa: E501
        :type: BillingAccountState
        """

        self._state = state

    @property
    def payment_terms(self):
        """Gets the payment_terms of this UpdateBillingAccountBodyBillingAccount.  # noqa: E501


        :return: The payment_terms of this UpdateBillingAccountBodyBillingAccount.  # noqa: E501
        :rtype: PaymentTerms
        """
        return self._payment_terms

    @payment_terms.setter
    def payment_terms(self, payment_terms):
        """Sets the payment_terms of this UpdateBillingAccountBodyBillingAccount.


        :param payment_terms: The payment_terms of this UpdateBillingAccountBodyBillingAccount.  # noqa: E501
        :type: PaymentTerms
        """

        self._payment_terms = payment_terms

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(UpdateBillingAccountBodyBillingAccount, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateBillingAccountBodyBillingAccount):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateBillingAccountBodyBillingAccount):
            return True

        return self.to_dict() != other.to_dict()
