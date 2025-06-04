TouchNet Marketplace

uPay® Technical

Guide

January 2025

> This document contains confidential information and may not be
> duplicated or disclosed to third parties, in whole or in part, for any
>
> purpose, without the prior express written consent of TouchNet
> Information Systems, Inc.
> Information represented in this document is subject to development and
> change without notice.
>
> Copyright 2025 TouchNet Information Systems, Inc.
>
> All rights reserved.
>
> TouchNet® and the TouchNet logo are trademarks of TouchNet Information
> Systems, Inc.
>
> Other trademarks within this document are the property of their
> respective owners. Other product or
>
> company names may be trademarks of their respective owners.
>
> *Document release date: January 2025*

i

> Contents

+-----------------------------------+-----------------------------------+
| > **1.0 Passing Parameters to     | > **1**\                          |
| > Your uPay Site**\               | > 12\                             |
| > 1.1 Workday Settings - Passing  | > **15**\                         |
| > Accounting Codes to uPay **2.0  | > 19\                             |
| > Using a Posting URL**\          | > **21**                          |
| > 2.1 About Recurring Payment     |                                   |
| > Parameters\                     |                                   |
| > **3.0 Passing Accounting Codes  |                                   |
| > to uPay**                       |                                   |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

ii



+-----------------------+-----------------------+-----------------------+
| > 1.0 Passing         |                       | 1                     |
| > Parameters to Your  |                       |                       |
| > uPay Site           |                       |                       |
+=======================+=======================+=======================+
| > 1.0                 | > Passing Parameters  |                       |
|                       | > to Your uPay Site   |                       |
+-----------------------+-----------------------+-----------------------+

> For uPay to integrate with a campus web application, the campus web
> application must be able to pass parameters that describe the
> transaction. At a minimum, the campus web application must pass a uPay
> site ID that identifies which uPay site will handle the transaction.
> In addition, in order for a transaction to be identified and tracked,
> the campus web application must pass a transaction ID (called
> EXT_TRANS_ID by uPay).
>
> Some parameters can be used to automatically populate fields on your
> uPay site. For example, the customer's billing address can be passed
> to uPay so that the customer isn't required to re-enter this
> information. Likewise, a dollar amount can be passed directly to uPay.
>
> You do not need to tell Marketplace which parameters you will be
> passing. You only need pass the parameters when directing a customer
> to your uPay site. uPay will accept any parameters that you pass and
> in turn pass the parameters back to your campus web application after
> the transaction is processed (provided you use the posting URL option,
> as described in **\"Using a Posting URL\" on page 15**).

+-----------------------------------+-----------------------------------+
| > uPay\                           | > In order for uPay to take       |
| > Parameter Details               | > action on passed parameters     |
|                                   | > (such as pre-populating the     |
|                                   | > billing address fields or the   |
|                                   | > dollar amount field), the       |
|                                   | > parameters must be named as     |
|                                   | > described below.                |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> If the campus web application passes recurring payment data---\
> RECURRING_USER_CAN_CHANGE, RECURRING_FREQUENCY,\
> RECURRING_START_DATE, and RECURRING_NUMBER_OF_PAYMENTS or
> RECURRING_END_DATE---to the uPay site, uPay will then take that data
> and calculate the payment schedule.
>
> **Note:** To receive back the payment parameters after the payment is
> completed in uPay, a posting URL must be used, as described in
> **\"Using a Posting URL\" on page 15**. If recurring payments are
> used, this payment information becomes critical for monitoring the
> payment process. For example, if recurring payment parameters are sent
> to the Posting URL, the campus web application will have a record of
> when the last payment is due.
>
> The following list describes all the parameters that uPay can use.
> uPay takes actions on the following parameters.
>
> **Parameters that uPay takes action upon once receiving:**

+-----------------+-----------------+-----------------+-----------------+
| >               | **Description** | **Field         | > **Data Type** |
|  **Parameters** |                 | Length**        |                 |
+=================+=================+=================+=================+
+-----------------+-----------------+-----------------+-----------------+

> Required. This is a numerical value unique to

+-----------------+-----------------+-----------------+-----------------+
| UPAY_SITE_ID    | each uPay site. | unlimited       | > numeric       |
|                 | The value is    |                 |                 |
|                 | displayed in    |                 |                 |
|                 | the             |                 |                 |
+=================+=================+=================+=================+
+-----------------+-----------------+-----------------+-----------------+

> Form Parameters page for the uPay site.
>
> CONFIDENTIAL
>
> uPay Technical Guide©2025 TouchNet Information Systems, Inc.


+-------------+-------------+-------------+-------------+-------------+
| 2           | > Chapter 3 | **De        | **Field     | > **Data    |
|             |             | scription** | Length**    | > Type**    |
+=============+=============+=============+=============+=============+
|             | > **P       |             |             |             |
|             | arameters** |             |             |             |
+-------------+-------------+-------------+-------------+-------------+

+-----------------+-----------------+-----------------+-----------------+
| BILL_NAME       | > Used to pass  | 50              | alphanumeric    |
|                 | > the billing   |                 |                 |
|                 | > name.         |                 |                 |
+=================+=================+=================+=================+
| BILL_EMAIL\_    | > Used to pass  | 50              | alphanumeric    |
|                 | > the billing   |                 |                 |
|                 | > e-mail        |                 |                 |
|                 | > address.      |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| > ADDRESS       |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| > BILL_STREET1  | > Used to pass  | 30              | alphanumeric    |
|                 | > the billing   |                 |                 |
|                 | > street        |                 |                 |
|                 | > address 1.    |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| > BILL_STREET2  | > Used to pass  | 30              | alphanumeric    |
|                 | > the billing   |                 |                 |
|                 | > street        |                 |                 |
|                 | > address 2.    |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| > BILL_CITY     | > Used to pass  | 35              | alphanumeric    |
|                 | > the billing   |                 |                 |
|                 | > city.         |                 |                 |
+-----------------+-----------------+-----------------+-----------------+

> Used to pass the billing state.
>
> The billing state should be passed as the two-\
> character state abbreviation. For foreign\
> addresses, \"\--\" can be passed to uPay in order to

+-----------------+-----------------+-----------------+-----------------+
| BILL_STATE      | > select \"Not  | 2               | alphanumeric    |
|                 | > applicable\"  |                 |                 |
|                 | > for the state |                 |                 |
|                 | > field.        |                 |                 |
+=================+=================+=================+=================+
+-----------------+-----------------+-----------------+-----------------+

> **Note:** If an invalid two-character state\
> abbreviation is passed, the default state as\
> established in the system administrative settings\
> will be used.
>
> Used to pass the billing postal code.

+-----------------+-----------------+-----------------+-----------------+
| > BILL_POSTAL\_ | To accommodate  | > 30            | alphanumeric    |
|                 | foreign         |                 |                 |
|                 | addresses, uPay |                 |                 |
|                 | will            |                 |                 |
+=================+=================+=================+=================+
| > CODE          | > accept up to  |                 |                 |
|                 | > 30 characters |                 |                 |
|                 | > in the postal |                 |                 |
|                 | > code          |                 |                 |
+-----------------+-----------------+-----------------+-----------------+

> parameter.
>
> Used to pass the two-letter country code for the\
> billing country.
>
> You must use the two-letter English language\
> country codes approved by the International\
> Organization for Standardization. This list can

+-----------------+-----------------+-----------------+-----------------+
| > BILL_COUNTRY  | > be found at   | 2               | alphabetic      |
|                 | > www.iso.or    |                 |                 |
|                 | g/iso/country\_ |                 |                 |
+=================+=================+=================+=================+
+-----------------+-----------------+-----------------+-----------------+

> codes.htm.
>
> **Note:** If an invalid two-character country\
> abbreviation is passed, the default country as\
> established in the system administrative settings\
> will be used.
>
> uPay Technical Guide\
> ©2025 TouchNet Information Systems, Inc.

CONFIDENTIAL


+-------------+-------------+-------------+-------------+-------------+
| > 1.0       |             | **Field     | > **Data    | 3           |
| > Passing   |             | Length**    | > Type**    |             |
| >           |             |             |             |             |
|  Parameters |             |             |             |             |
| > to Your   |             |             |             |             |
| > uPay Site |             |             |             |             |
+=============+=============+=============+=============+=============+
| > **P       | **De        |             |             |             |
| arameters** | scription** |             |             |             |
+-------------+-------------+-------------+-------------+-------------+

> Optional. The value for this parameter is\
> generated by the campus web application. It\
> serves as a cross-reference between the web\
> application and Marketplace. If this parameter is\
> passed to uPay, it will be stored in the\
> Marketplace database along with information\
> about the transaction.
>
> If the campus web application passes the\
> VALIDATION_KEY parameter (and Yes for\
> \"Require encoded validation key for amount?\"\
> is selected on the uPay Payment Settings page),\
> then you MUST pass the EXT_TRANS_ID\
> parameter.
>
> This field does not appear if you selected Yes\
> for \"Site uses T-Link\" on the uPay Payment\
> Settings page.

+-----------------+-----------------+-----------------+-----------------+
| > EXT_TRANS_ID  | > If Yes is     | > 250           | alphanumeric    |
|                 | > selected for  |                 |                 |
|                 | > \"Validate    |                 |                 |
|                 | > External      |                 |                 |
+=================+=================+=================+=================+
|                 | Transaction ID  |                 |                 |
|                 | is unique to    |                 |                 |
|                 | this uPay       |                 |                 |
|                 | site?\" on      |                 |                 |
+-----------------+-----------------+-----------------+-----------------+

> the uPay Payment Settings page, uPay will\
> require that an EXT_TRANS_ID is passed by the\
> campus web application. In this case, the EXT\_\
> TRANS_ID value must be unique for this uPay\
> site. uPay will validate that the submitted\
> external transaction ID has not previously been\
> used. (However, this EXT_TRANS_ID value\
> CAN be used by other uPay sites.) If this value\
> is not passed, or if the value is not unique, the\
> customer will receive an error message.
>
> Use of the EXT_TRANS_ID parameter allows\
> you to use Marketplace's uPay Payment Search\
> functionality to search for payments with a\
> specified EXT_TRANS_ID value. In addition,\
> you will be able to view the EXT_TRANS_ID\
> values on Marketplace's Posting Status Report.
>
> Optional. This field can contain a description of\
> the EXT_TRANS_ID value. If this parameter is

+-----------------+-----------------+-----------------+-----------------+
| EXT_TRANS\_     | used *and       | unlimited       | > alphanumeric  |
|                 | EXT_TRANS_ID is |                 |                 |
|                 | also passed*,   |                 |                 |
|                 | this            |                 |                 |
+=================+=================+=================+=================+
| > ID_LABEL      | > description   |                 |                 |
|                 | > appears on    |                 |                 |
|                 | > the receipt   |                 |                 |
|                 | > that the cus- |                 |                 |
+-----------------+-----------------+-----------------+-----------------+

> tomer sees at the end of the uPay payment pro-\
> cess. HTML is NOT allowed in this field.
>
> CONFIDENTIAL
>
> uPay Technical Guide©2025 TouchNet Information Systems, Inc.



+-------------+-------------+-------------+-------------+-------------+
| 4           | > Chapter 3 | **De        | **Field     | > **Data    |
|             |             | scription** | Length**    | > Type**    |
+=============+=============+=============+=============+=============+
|             | > **P       |             |             |             |
|             | arameters** |             |             |             |
+-------------+-------------+-------------+-------------+-------------+

> Optional. If used, this parameter automatically\
> completes the Payment Amount field when the\
> customer arrives at the uPay site. To use this\
> parameter, you must configure your uPay site\
> by selecting Yes for \"Allow the amount to be\
> passed in\" on the uPay Payment Settings page.

+-----------------+-----------------+-----------------+-----------------+
| > AMT           | If the campus   | 8 (including    | > numeric       |
|                 | web application |                 |                 |
|                 | passes the      |                 |                 |
+=================+=================+=================+=================+
|                 |                 | 2 characters    |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 | VALIDATION_KEY  |                 |                 |
|                 | parameter (and  |                 |                 |
|                 | Yes for         |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 |                 | to the right    |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 | > \"Require     |                 |                 |
|                 | > encoded       |                 |                 |
|                 | > validation    |                 |                 |
|                 | > key for       |                 |                 |
|                 | > amount?\"     |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 |                 | > of the        |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 | > is selected   |                 |                 |
|                 | > on the uPay   |                 |                 |
|                 | > Payment       |                 |                 |
|                 | > Settings      |                 |                 |
|                 | > page),        |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 |                 | > decimal       |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 | then you MUST   |                 |                 |
|                 | pass the AMT    |                 |                 |
|                 | parameter.      |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 |                 | > point)        |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 | > By default,   |                 |                 |
|                 | > T-Link        |                 |                 |
|                 | > expects the   |                 |                 |
|                 | > payment       |                 |                 |
|                 | > amount        |                 |                 |
+-----------------+-----------------+-----------------+-----------------+

> to be passed with the AMT parameter from the\
> web application. If a payment amount is not\
> passed, the uPay site\'s default payment amount\
> will be displayed to the customer.
>
> Maximum value: 99999.99.
>
> This parameter can be used only used if you\
> accept ACH payments. This is the Shared Secret\
> Value that the user enters on the ACH\
> agreement page when paying by checking or\
> savings account.

+-----------------+-----------------+-----------------+-----------------+
| SSV             | > A shared      | unlimited       | alphanumeric    |
|                 | > secret value  |                 |                 |
|                 | > is an         |                 |                 |
|                 | > alphanumeric  |                 |                 |
|                 | > value         |                 |                 |
+=================+=================+=================+=================+
|                 | > that the user |                 |                 |
|                 | > knows, for    |                 |                 |
|                 | > example,      |                 |                 |
|                 | > their birth   |                 |                 |
+-----------------+-----------------+-----------------+-----------------+

> year or their mother's maiden name. While the\
> shared secret value is not required by uPay, it is\
> a requirement of the NACHA rules for web-\
> based ACH payments. Having users enter a\
> shared secret value increases security of\
> payments through electronic bank accounts.
>
> This parameter can only be used if you accept\
> ACH payments. The SSV_PROMPT is used\
> when the user pays by checking or savings\
> account. If passed, it overrides your setting for

+-----------------+-----------------+-----------------+-----------------+
| > SSV_PROMPT    | > the Shared    | > unlimited     | alphanumeric    |
|                 | > Secret Value  |                 |                 |
|                 | > prompt. This  |                 |                 |
|                 | > is the        |                 |                 |
+=================+=================+=================+=================+
+-----------------+-----------------+-----------------+-----------------+

> prompt shown to users so they know what to\
> enter for the Shared Secret value. If the prompt\
> value is not passed, uPay uses the prompt you\
> define in the Payment Method Settings page.
>
> uPay Technical Guide\
> ©2025 TouchNet Information Systems, Inc.

CONFIDENTIAL


+-------------+-------------+-------------+-------------+-------------+
| > 1.0       |             | **Field     | > **Data    | 5           |
| > Passing   |             | Length**    | > Type**    |             |
| >           |             |             |             |             |
|  Parameters |             |             |             |             |
| > to Your   |             |             |             |             |
| > uPay Site |             |             |             |             |
+=============+=============+=============+=============+=============+
| > **P       | **De        |             |             |             |
| arameters** | scription** |             |             |             |
+-------------+-------------+-------------+-------------+-------------+

> If the uPay site has been configured to accept a\
> passed amount from the campus web\
> application, TouchNet recommends that the\
> VALIDATION_KEY parameter also be passed.\
> The use of an encoded validation key helps to\
> ensure the integrity of amounts that are passed\
> to uPay.
>
> In order to pass a VALIDATION_KEY, the\
> following actions must be taken:
>
> ●The \"Require encoded validation key for\
> amount?\" field on the uPay Payment Settings

+-----------------+-----------------+-----------------+-----------------+
| VALIDATION\_    | > page must be  | unlimited       | > alphanumeric  |
|                 | > set to Yes.   |                 |                 |
+=================+=================+=================+=================+
|                 | ●You must enter |                 |                 |
|                 | a \"Passed      |                 |                 |
|                 | Amount          |                 |                 |
|                 | Validation      |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| > KEY           |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 | Key\" value on  |                 |                 |
|                 | the uPay        |                 |                 |
|                 | Payment         |                 |                 |
|                 | Settings        |                 |                 |
+-----------------+-----------------+-----------------+-----------------+

> page.
>
> ●The campus web application must pass a\
> transaction amount (AMT) as an input\
> parameter.
>
> ●The campus web application must pass an\
> external transaction ID (EXT_TRANS_ID) as\
> an input parameter.
>
> ●The campus web application must determine\
> the value for the VALIDATION_KEY\
> parameter.
>
> If any part of this configuration has not been\
> completed, uPay will not accept the payment.

+-----------------+-----------------+-----------------+-----------------+
| > ADD_ON\_      | If the display  | unlimited       | > alphanumeric  |
|                 | of an           |                 |                 |
|                 | Additional      |                 |                 |
|                 | Donation has    |                 |                 |
+=================+=================+=================+=================+
|                 | > been turned   |                 |                 |
|                 | > on in the     |                 |                 |
|                 | > uPay site     |                 |                 |
|                 | >               |                 |                 |
|                 |  configuration, |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| > OFFER\_       |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 | > the           |                 |                 |
|                 | > Additional    |                 |                 |
|                 | > Donation can  |                 |                 |
|                 | > be turned off |                 |                 |
|                 | > by            |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| > DISABLED      |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 | passing         |                 |                 |
|                 | **true** as the |                 |                 |
|                 | value for this  |                 |                 |
|                 | parameter.      |                 |                 |
+-----------------+-----------------+-----------------+-----------------+

> CONFIDENTIAL
>
> uPay Technical Guide©2025 TouchNet Information Systems, Inc.


+-------------+-------------+-------------+-------------+-------------+
| 6           | > Chapter 3 | **De        | **Field     | > **Data    |
|             |             | scription** | Length**    | > Type**    |
+=============+=============+=============+=============+=============+
|             | > **P       |             |             |             |
|             | arameters** |             |             |             |
+-------------+-------------+-------------+-------------+-------------+

> Optional. In order to establish recurring\
> payments, this parameter MUST be passed.
>
> This parameter determines whether the\
> customer can change the recurring payment\
> values that are passed by the campus web

+-----------------+-----------------+-----------------+-----------------+
| > RECURRING\_   | application.    | > unlimited     | alphanumeric    |
|                 | Accepted        |                 |                 |
|                 | values: True or |                 |                 |
|                 | False.          |                 |                 |
+=================+=================+=================+=================+
| USER_CAN\_      | > **Note:** If  |                 |                 |
|                 | > RECUR         |                 |                 |
|                 | RING_USER_CAN\_ |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| > CHANGE        |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 | > CHANGE=false, |                 |                 |
|                 | > uPay must     |                 |                 |
|                 | > receive       |                 |                 |
+-----------------+-----------------+-----------------+-----------------+

> RECURRING_START_DATE, RECURRING\_\
> FREQUENCY and RECURRING_END_DATE or\
> RECURRING_NUMBER_OF_PAYMENTS. If\
> uPay does not receive these values, uPay will\
> display an error message to the customer.
>
> uPay Technical Guide\
> ©2025 TouchNet Information Systems, Inc.

CONFIDENTIAL


+-------------+-------------+-------------+-------------+-------------+
| > 1.0       |             | **Field     | > **Data    | 7           |
| > Passing   |             | Length**    | > Type**    |             |
| >           |             |             |             |             |
|  Parameters |             |             |             |             |
| > to Your   |             |             |             |             |
| > uPay Site |             |             |             |             |
+=============+=============+=============+=============+=============+
| > **P       | **De        |             |             |             |
| arameters** | scription** |             |             |             |
+-------------+-------------+-------------+-------------+-------------+

> If recurring payment parameters are being sent to the\
> uPay site, this parameter determines what happens if\
> the customer enters a payment card expiration date\
> that will occur *before* the projected end date of the\
> recurring payments. Accepted values: Yes or No.
>
> If RECURRING_EXP_DATE_CHANGE=Yes and the\
> customer enters a payment card expiration date that\
> will occur before the projected end date of the\
> recurring payments, uPay will automatically change\
> the end date of the recurring payments so it comes\
> before the payment card expiration date. If\
> RECURRING_EXP_DATE_CHANGE=No and the\
> customer enters a payment card expiration date that\
> will occur before the projected end date of the\
> recurring payments, uPay will prompt the customer\
> to use a different payment card.
>
> **Example:** The customer uses the campus web\
> application to make a monthly donation of \$100. In

+-----------------+-----------------+-----------------+-----------------+
| > RECURRING\_   | the campus web  | > unlimited     | > alphanumeric  |
|                 | application,    |                 |                 |
|                 | the customer    |                 |                 |
|                 | enters the      |                 |                 |
+=================+=================+=================+=================+
|                 | > following     |                 |                 |
|                 | > information   |                 |                 |
|                 | > when          |                 |                 |
|                 | > establishing  |                 |                 |
|                 | > recurring     |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| > CAN_CHANGE\_  |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 | > payments:     |                 |                 |
|                 | > start date -  |                 |                 |
|                 | > 10/26/2008,   |                 |                 |
|                 | > frequency -   |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| > END_DATE\_    | monthly, and    |                 |                 |
|                 | end date -      |                 |                 |
|                 | 06/26/10. This  |                 |                 |
|                 | information is  |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| > TO_CC_EXP\_   | > passed to     |                 |                 |
|                 | > uPay by the   |                 |                 |
|                 | > campus web    |                 |                 |
|                 | > application,  |                 |                 |
|                 | > at            |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| > DATE          | > which point   |                 |                 |
|                 | > the customer  |                 |                 |
|                 | > enters their  |                 |                 |
|                 | > payment card  |                 |                 |
+-----------------+-----------------+-----------------+-----------------+

> information. The customer enters a payment card\
> expiration date of 04/10---which predates the end\
> date of the recurring payments. Because the campus\
> web application sent RECURRING_EXP_DATE\_\
> CHANGE=Yes, uPay automatically changes the date\
> of the last payment to 4/26/10. The monthly donation\
> remains unchanged at \$100.
>
> **Note:** RECURRING_CAN_CHANGE_END_DATE\_\
> TO_CC_EXP_DATE=Yes should only be used in\
> situations in which it is acceptable that the total\
> dollar amount of recurring payments can be reduced\
> by the elimination of one or more payments.
>
> RECURRING_CAN_CHANGE_END_DATE_TO_CC\_\
> EXP_DATE=Yes might work well with donations, in\
> which the alternative of the customer canceling the\
> recurring payments would be less desirable than the\
> elimination of one or more individual payments. In\
> contrast, the elimination of payments for a product\
> that is actually delivered to the customer, such as a
>
> CONFIDENTIAL
>
> uPay Technical Guide©2025 TouchNet Information Systems, Inc.


+-------------+-------------+-------------+-------------+-------------+
| 8           | > Chapter 3 | **De        | **Field     | > **Data    |
|             |             | scription** | Length**    | > Type**    |
+=============+=============+=============+=============+=============+
|             | > **P       |             |             |             |
|             | arameters** |             |             |             |
+-------------+-------------+-------------+-------------+-------------+

> parking pass or a football season ticket, would most
>
> likely be considered unacceptable.
>
> If the uPay site accepts recurring payments, this\
> parameter determines the start date for the recur-

+-----------------+-----------------+-----------------+-----------------+
| > RECURRING\_   | > ring          | > 10            | alphanumeric    |
|                 | > payments. The |                 |                 |
|                 | > customer must |                 |                 |
|                 | > enter         |                 |                 |
|                 | > today\'s      |                 |                 |
+=================+=================+=================+=================+
| > START_DATE    | > date or a     |                 |                 |
|                 | > later date    |                 |                 |
|                 | > (i.e., the    |                 |                 |
|                 | > customer      |                 |                 |
|                 | > cannot        |                 |                 |
+-----------------+-----------------+-----------------+-----------------+

> enter a past date). Required date format: mm/d-\
> d/yyyy.
>
> If the uPay site accepts recurring payments, this\
> parameter determines the end date for the recur-\
> ring payments. Any value passed in this field

+-----------------+-----------------+-----------------+-----------------+
| > RECURRING\_   | will override   | > 10            | alphanumeric    |
|                 | the Maximum     |                 |                 |
|                 | Duration as     |                 |                 |
|                 | con-            |                 |                 |
+=================+=================+=================+=================+
| END_DATE        | figured in the  |                 |                 |
|                 | Recurring       |                 |                 |
|                 | Settings for    |                 |                 |
|                 | this uPay       |                 |                 |
+-----------------+-----------------+-----------------+-----------------+

> site. Required date format: mm/dd/yyyy. (Max-\
> imum accepted value is 99 years from the start\
> date.)
>
> If the uPay site accepts recurring payments, this\
> parameter sets the frequency of the scheduled\
> payments. Accepted values: 1 (Monthly), 2 ( Bi-\
> Monthly), 4 (Weekly), 5 (Quarterly), 6 (Semi-

+-----------------+-----------------+-----------------+-----------------+
| > RECURRING\_   | > Annually), 7  | unlimited       | > numeric       |
|                 | > (Annually),   |                 |                 |
|                 | > and 9         |                 |                 |
|                 | > (Daily).      |                 |                 |
+=================+=================+=================+=================+
| FREQUENCY       | **Note:** For   |                 |                 |
|                 | RECUR           |                 |                 |
|                 | RING_FREQUENCY, |                 |                 |
|                 | be sure         |                 |                 |
+-----------------+-----------------+-----------------+-----------------+

> to use the accepted numerical values. For\
> example, to set up weekly recurring payments,\
> send RECURRING_FREQUENCY=4; Do not\
> send RECURRING_FREQUENCY=Weekly.
>
> If the uPay site accepts recurring payments, this\
> parameter determines the number of scheduled\
> recurring payments. Any value passed in this\
> field will override the Maximum Duration as

+-----------------+-----------------+-----------------+-----------------+
| > RECURRING\_   | > configured in | > unlimited     | > numeric       |
|                 | > the Recurring |                 |                 |
|                 | > Settings for  |                 |                 |
|                 | > this          |                 |                 |
+=================+=================+=================+=================+
|                 | uPay site.      |                 |                 |
|                 | (Maximum        |                 |                 |
|                 | accepted value  |                 |                 |
|                 | is 99 years     |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| > NUMBER_OF\_   |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 | > from the      |                 |                 |
|                 | > start date.)  |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| > PAYMENTS      |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 | > **Note:** If  |                 |                 |
|                 | > both          |                 |                 |
|                 | > RECURR        |                 |                 |
|                 | ING_NUMBER_OF\_ |                 |                 |
+-----------------+-----------------+-----------------+-----------------+

> PAYMENTS and RECURRING_END_DATE are\
> passed to uPay, uPay will use RECURRING\_\
> NUMBER_OF_PAYMENTS to calculate the\
> payment schedule.
>
> uPay Technical Guide\
> ©2025 TouchNet Information Systems, Inc.

CONFIDENTIAL



+-------------+-------------+-------------+-------------+-------------+
| > 1.0       |             | **Field     | > **Data    | 9           |
| > Passing   |             | Length**    | > Type**    |             |
| >           |             |             |             |             |
|  Parameters |             |             |             |             |
| > to Your   |             |             |             |             |
| > uPay Site |             |             |             |             |
+=============+=============+=============+=============+=============+
| > **P       | **De        |             |             |             |
| arameters** | scription** |             |             |             |
+-------------+-------------+-------------+-------------+-------------+

+-----------------+-----------------+-----------------+-----------------+
| CONTINUE\_      | > Optional.     | unlimited       | > alphanumeric  |
|                 | > This          |                 |                 |
|                 | > parameter can |                 |                 |
|                 | > be used for   |                 |                 |
+=================+=================+=================+=================+
|                 | passing the     |                 |                 |
|                 | alternative     |                 |                 |
|                 | text to be      |                 |                 |
|                 | displayed as    |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| > LINK_TEXT     |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 | > the Continue  |                 |                 |
|                 | > link in the   |                 |                 |
|                 | > uPay site.    |                 |                 |
+-----------------+-----------------+-----------------+-----------------+

> Optional. When you establish a uPay site, you\
> enter a URL for the success link that appears on\
> the receipt page the customer sees after suc-\
> cessfully making a uPay payment. Instead of

+-----------------+-----------------+-----------------+-----------------+
| > SUCCESS_LINK  | providing the   | unlimited       | > alphanumeric  |
|                 | same URL for    |                 |                 |
|                 | all customers,  |                 |                 |
|                 | you             |                 |                 |
+=================+=================+=================+=================+
|                 | > can customize |                 |                 |
|                 | > the success   |                 |                 |
|                 | > link URL. For |                 |                 |
+-----------------+-----------------+-----------------+-----------------+

> example, for customers identified as students,\
> you might return them to a student portal web\
> site, while parents might be returned to a portal\
> designed for the parents of students.
>
> Optional. This text appears as a hyperlink on\
> the receipt page that customers see after suc-

+-----------------+-----------------+-----------------+-----------------+
| >               | > cessfully     | unlimited       | > alphanumeric  |
|  SUCCESS_LINK\_ | > making a      |                 |                 |
|                 | > payment with  |                 |                 |
|                 | > uPay. While   |                 |                 |
+=================+=================+=================+=================+
|                 | > the           |                 |                 |
|                 | > SUCCESS_LINK  |                 |                 |
|                 | > parameter     |                 |                 |
|                 | > provides the  |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| > TEXT          |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 | > URL for the   |                 |                 |
|                 | > hyperlink,    |                 |                 |
|                 | > the           |                 |                 |
|                 | >               |                 |                 |
|                 |  SUCCESS_LINK\_ |                 |                 |
+-----------------+-----------------+-----------------+-----------------+

> TEXT parameter provides the text for the hyper-\
> link.
>
> Optional. When you establish a uPay site, you\
> enter a URL for the error link that appears on\
> the error page that the customer sees when a

+-----------------+-----------------+-----------------+-----------------+
| ERROR_LINK      | system error    | unlimited       | > alphanumeric  |
|                 | occurs while    |                 |                 |
|                 | attempting to   |                 |                 |
|                 | make            |                 |                 |
+=================+=================+=================+=================+
+-----------------+-----------------+-----------------+-----------------+

> payment. Instead of providing the same URL for\
> all customers, you can customize the link that\
> appears when an error is encountered.
>
> Optional. This text appears as a hyperlink on\
> the error page that customers see after a system

+-----------------+-----------------+-----------------+-----------------+
| ERROR_LINK\_    | > error occurs  | unlimited       | > alphanumeric  |
|                 | > while         |                 |                 |
|                 | > attempting to |                 |                 |
|                 | > make a pay-   |                 |                 |
+=================+=================+=================+=================+
|                 | ment with uPay. |                 |                 |
|                 | While the       |                 |                 |
|                 | ERROR_LINK      |                 |                 |
|                 | para-           |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| > TEXT          |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 | meter provides  |                 |                 |
|                 | the URL for the |                 |                 |
|                 | hyperlink, the  |                 |                 |
+-----------------+-----------------+-----------------+-----------------+

> ERROR_LINK_TEXT parameter provides the text\
> for the hyperlink.
>
> Optional. When you establish a uPay site, you\
> enter a URL for the cancel link that appears

+-----------------+-----------------+-----------------+-----------------+
| > CANCEL_LINK   | throughout your | unlimited       | > alphanumeric  |
|                 | uPay site.      |                 |                 |
|                 | Instead of      |                 |                 |
|                 | providing       |                 |                 |
+=================+=================+=================+=================+
|                 | > the same URL  |                 |                 |
|                 | > for all       |                 |                 |
|                 | > customers,    |                 |                 |
|                 | > you can cus-  |                 |                 |
+-----------------+-----------------+-----------------+-----------------+

> tomize the link that appears when an error is\
> encountered.
>
> CONFIDENTIAL
>
> uPay Technical Guide©2025 TouchNet Information Systems, Inc.


+-------------+-------------+-------------+-------------+-------------+
| 10          | > Chapter 3 | **De        | **Field     | > **Data    |
|             |             | scription** | Length**    | > Type**    |
+=============+=============+=============+=============+=============+
|             | > **P       |             |             |             |
|             | arameters** |             |             |             |
+-------------+-------------+-------------+-------------+-------------+

> Optional. This text appears when a uPay cus-\
> tomer places their cursor over the Cancel but-

+-----------------+-----------------+-----------------+-----------------+
| > CANCEL_LINK\_ | > ton. (Only    | unlimited       | alphanumeric    |
|                 | > works with    |                 |                 |
|                 | > Microsoft     |                 |                 |
|                 | > Internet      |                 |                 |
+=================+=================+=================+=================+
|                 | > Explorer.) In |                 |                 |
|                 | > the HTML for  |                 |                 |
|                 | > the uPay      |                 |                 |
|                 | > site, this    |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| > TEXT          |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 | text is added   |                 |                 |
|                 | as the ALT      |                 |                 |
|                 | attribute of    |                 |                 |
|                 | the Cancel      |                 |                 |
+-----------------+-----------------+-----------------+-----------------+

> button (which appears in the HTML as an IMG\
> tag).
>
> Used to pass a credit accounting code. This\
> value will override the credit accounting code\
> that was entered when the uPay site was con-\
> figured. This value must be an approved code

+-----------------+-----------------+-----------------+-----------------+
| > CREDIT_ACCT\_ | for the general | > unlimited     | alphanumeric    |
|                 | ledger system.  |                 |                 |
|                 | Additional      |                 |                 |
|                 | credit          |                 |                 |
+=================+=================+=================+=================+
|                 | > account codes |                 |                 |
|                 | > may be passed |                 |                 |
|                 | > with \_#      |                 |                 |
|                 | > appen-        |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| > CODE          |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 | ded to the      |                 |                 |
|                 | C               |                 |                 |
|                 | REDIT_ACCT_CODE |                 |                 |
|                 | and CREDIT\_    |                 |                 |
+-----------------+-----------------+-----------------+-----------------+

> ACCT_AMT parameters (examples: CREDIT\_\
> ACCT_CODE_2 and CREDIT_ACCT_AMT_2). If\
> multiple account codes are passed, CREDIT\_\
> ACCT_CODE must be passed.
>
> Used to pass a debit accounting code. This

+-----------------+-----------------+-----------------+-----------------+
| > DEBIT_ACCT\_  | > value will    | > unlimited     | alphanumeric    |
|                 | > override the  |                 |                 |
|                 | > debit         |                 |                 |
|                 | > accounting    |                 |                 |
|                 | > code          |                 |                 |
+=================+=================+=================+=================+
|                 | > that was      |                 |                 |
|                 | > entered in    |                 |                 |
|                 | > Payment       |                 |                 |
|                 | > Gateway as    |                 |                 |
|                 | > the           |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| > CODE          |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 | > Host Payment  |                 |                 |
|                 | > Method ID for |                 |                 |
|                 | > this uPay     |                 |                 |
|                 | > site. This    |                 |                 |
+-----------------+-----------------+-----------------+-----------------+

> value must be an approved general ledger code.
>
> When passing multiple accounting codes, this\
> parameter is used to pass the amount to be asso-\
> ciated with the corresponding credit account\
> code (CREDIT_ACCT_CODE). If CREDIT\_

+-----------------+-----------------+-----------------+-----------------+
| > CREDIT_ACCT\_ | > ACCT_AMT is   | unlimited       | alphanumeric    |
|                 | > passed,       |                 |                 |
|                 | > C             |                 |                 |
|                 | REDIT_ACCT_CODE |                 |                 |
+=================+=================+=================+=================+
| > AMT           | must also be    |                 |                 |
|                 | passed.         |                 |                 |
|                 | Additional      |                 |                 |
|                 | credit account  |                 |                 |
+-----------------+-----------------+-----------------+-----------------+

> amounts may be passed with \_# appended to\
> the CREDIT_ACCT_CODE and CREDIT_ACCT\_\
> AMT parameters (examples: CREDIT_ACCT\_\
> CODE_2 and CREDIT_ACCT_AMT_2).
>
> uPay Technical Guide\
> ©2025 TouchNet Information Systems, Inc.

CONFIDENTIAL


+-------------+-------------+-------------+-------------+-------------+
| > 1.0       |             | **Field     | > **Data    | 11          |
| > Passing   |             | Length**    | > Type**    |             |
| >           |             |             |             |             |
|  Parameters |             |             |             |             |
| > to Your   |             |             |             |             |
| > uPay Site |             |             |             |             |
+=============+=============+=============+=============+=============+
| > **P       | **De        |             |             |             |
| arameters** | scription** |             |             |             |
+-------------+-------------+-------------+-------------+-------------+

> When passing multiple accounting codes, this\
> parameter is used to pass the amount to asso-\
> ciate with the corresponding credit account\
> code (CREDIT_ACCT_CODE_2). If this para-

+-----------------+-----------------+-----------------+-----------------+
| > CREDIT_ACCT\_ | meter is        | unlimited       | > alphanumeric  |
|                 | passed,         |                 |                 |
|                 | CRE             |                 |                 |
|                 | DIT_ACCT_CODE_2 |                 |                 |
|                 | must            |                 |                 |
+=================+=================+=================+=================+
| > AMT_2         | > also be       |                 |                 |
|                 | > passed.       |                 |                 |
|                 | > Additional    |                 |                 |
|                 | > credit        |                 |                 |
|                 | > account       |                 |                 |
+-----------------+-----------------+-----------------+-----------------+

> amounts may be passed using the same naming\
> convention (Example: CREDIT_ACCT_AMT_3).
>
> The sum of these amounts must equal the\
> amount passed with the AMT parameter.
>
> This parameter can be used to pass an addi-\
> tional accounting code. If this parameter is\
> passed, CREDIT_ACCT_AMT_2 must also be\
> passed. Additional credit account codes may be\
> passed using the same naming format.
>
> (Example: CREDIT_ACCT_CODE_3.) Whenever

+-----------------+-----------------+-----------------+-----------------+
| > CREDIT_ACCT\_ | > CRED          | unlimited       | > alphanumeric  |
|                 | IT_ACCT_CODE\_# |                 |                 |
|                 | > is passed, a  |                 |                 |
|                 | > cor-          |                 |                 |
+=================+=================+=================+=================+
| > CODE_2        | > responding    |                 |                 |
|                 | > CRE           |                 |                 |
|                 | DIT_ACCT_AMT\_# |                 |                 |
|                 | > must be       |                 |                 |
+-----------------+-----------------+-----------------+-----------------+

> passed to specify the amount. Any additional\
> credit accounting codes passed must be in\
> numerical sequence (i.e., don\'t skip any num-\
> bers). There is no limit to the number of credit\
> accounting codes that can be passed as input\
> parameters.

+-----------------+-----------------+-----------------+-----------------+
| > ADD_ON\_      | This parameter  | > unlimited     | > alphanumeric  |
|                 | is used to pass |                 |                 |
|                 | an override     |                 |                 |
|                 | value           |                 |                 |
+=================+=================+=================+=================+
| > OFFER\_       | > for the       |                 |                 |
|                 | > Additional    |                 |                 |
|                 | > Donation      |                 |                 |
|                 | > accounting    |                 |                 |
|                 | > code          |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| > CREDIT_ACCT\_ | (only used if   |                 |                 |
|                 | Additional      |                 |                 |
|                 | Donation is     |                 |                 |
|                 | enabled in      |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| > CODE          | > the uPay site |                 |                 |
|                 | > settings).    |                 |                 |
+-----------------+-----------------+-----------------+-----------------+

> In addition to the parameters described above, the campus web
> application can send\
> additional parameters. The campus merchant can configure any of these
> parameters to be \[additional available in Marketplace reports and
> orders parameters\] search, as described in **\"Form Parameters\" on
> page 1**. uPay will take no additional actions on these parameters
> other than to return these parameters to the Posting URL, as described
> in **\"Using a Posting URL\" on page 15**).
>
> CONFIDENTIAL
>
> uPay Technical Guide©2025 TouchNet Information Systems, Inc.

+-----------------------+-----------------------+-----------------------+
| 12                    | > Chapter 3           | > Workday Settings -  |
|                       |                       | > Passing Accounting  |
|                       |                       | > Codes               |
+=======================+=======================+=======================+
|                       | 1.1                   |                       |
+-----------------------+-----------------------+-----------------------+

> to uPay
>
> *If you use Workday, please review this section for XML parameters
> that you will need to set up.*
>
> You can pass parameters from a campus web application to your uPay
> site, as described in **\"Passing Parameters to Your uPay Site\" on
> page 1**as described in the *Marketplace User Guide*. For the
> CREDIT_ACCT_CODE parameter, you must pass a Ledger ID and all
> applicable Worktags and their values. You must pass these values with
> valid XML. CREDIT_ACCT\_\
> AMT must also be passed.

+-----------------------------------------------------------------------+
| > ***Important!*** When you pass the CREDIT_ACCT_CODE parameter, none |
| > of the values associated with the uPay site\'s assigned Marketplace |
| > accounting code will be used, so you must ensure that you send a    |
| > complete set of Workday general ledger data.                        |
+=======================================================================+
+-----------------------------------------------------------------------+

> Additional sets of data may be sent with CREDIT_ACCT_CODE\_#\
> (example: CREDIT_ACCT_CODE_2) Whenever CREDIT_ACCT_CODE\_# is passed,
> a corresponding CREDIT_ACCT_AMT\_# must be passed to specify the
> amount. Any additional credit accounting codes passed must be in
> numerical sequence (i.e., don\'t skip any numbers). There is no limit
> to the number of credit accounting codes that can be passed as input
> parameters.

Here is an example of XML passed for the CREDIT_ACCT_CODE field:

> \<ACCOUNT_INFO\>\
> \<LEDGER id=\"54000\"\>\
> \<PARENT /\>\
> \</LEDGER\>\
> \<SPEND_CATEGORY /\>\
> \<REVENUE_CATEGORY /\>\
> \<WORKTAG type=\"Spend_Category_ID\"\>Spend_Cat_Office\_
> Supplies\</WORKTAG\>\
> \<WORKTAG type=\"Business_Unit_ID\"\>42\</WORKTAG\> \<WORKTAG
> type=\"Cost_Center_Reference_ID\"\>CC\_\
> 43010\</WORKTAG\>\
> \<WORKTAG type=\"Catalog_Item_ID\" /\>\
> \<WORKTAG type=\"Job_Level_ID\" /\>\
> \<WORKTAG type=\"Gift_Reference_ID\"\>00000\</WORKTAG\> \<WORKTAG
> type=\"Fund_ID\"\>10\</WORKTAG\>\
> \</ACCOUNT_INFO\>
>
> The following rules must be followed when passing XML for the CREDIT\_
> ACCT_CODE parameter:
>
> uPay Technical Guide\
> ©2025 TouchNet Information Systems, Inc.

CONFIDENTIAL

+-----------------------+-----------------------+-----------------------+
| > 1.0 Passing         |                       | 13                    |
| > Parameters to Your  |                       |                       |
| > uPay Site           |                       |                       |
+=======================+=======================+=======================+
| ●                     | The entire set of XML |                       |
|                       | must be wrapped with  |                       |
|                       | \<ACCOUNT_INFO\>      |                       |
+-----------------------+-----------------------+-----------------------+

and \</ACCOUNT_INFO\>

> ● The XML can be one string or multiple lines.
>
> ● Any number of WORKTAG fields can be passed, but the name of the
> Worktag must be specified in the \"type\" field and the value must be
> specified between the open and close WORKTAG tags.
>
> ● A value for LEDGER must be passed in the \"id\" field or a GL
> exception will occur.
>
> ● Values for SPEND_CATEGORY and REVENUE_CATEGORY may optionally be
> passed. The values for these tags must be passed between the
> corresponding open and close tags.
>
> ● The passed XML must not exceed 2000 total characters.
>
> If you do not know what values to enter, be sure to contact your
> Workday administrator.
>
> The value that you enter is not validated by uPay, so you must make
> sure you enter valid Workday values.
>
> **Note:** If the campus web application passes an incomplete or
> incorrect value for the CREDIT_ACCT_CODE parameter, the transaction
> will still be accepted (provided the customer enters valid payment
> information); however, a GL exception will be generated. A uPay site
> manager should resolve any GL exceptions that result.

+-----------------------------------------------------------------------+
| > ***Important!*** The DEBIT_ACCT_CODE parameter cannot be passed to  |
| > uPay when Workday general ledger integration is used. uPay sites    |
| > will always pass the value configured in the uPay site\'s \"Bank    |
| > Account ID\" field when reporting a value for                       |
| > Bank_Account_Reference to Workday.                                  |
+=======================================================================+
+-----------------------------------------------------------------------+

> CONFIDENTIAL
>
> uPay Technical Guide©2025 TouchNet Information Systems, Inc.

+-----------------------------------+-----------------------------------+
| 14                                | > Chapter 3                       |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> uPay Technical Guide\
> ©2025 TouchNet Information Systems, Inc.

CONFIDENTIAL



+-----------------------+-----------------------+-----------------------+
| > 2.0 Using a Posting |                       | 15                    |
| > URL                 |                       |                       |
+=======================+=======================+=======================+
| > 2.0                 | > Using a Posting URL |                       |
+-----------------------+-----------------------+-----------------------+

> After a transaction is processed (or recurring payments are
> scheduled), uPay can pass parameters describing the transaction back
> to a campus web application. This information can include parameters
> that were initially passed to uPay from a web application, such as a
> payment amount or a transaction ID. These parameters can include
> information about the status of the transaction (as determined by
> Payment Gateway). When this\
> information is posted, the status of the transaction can be updated in
> the campus web application.
>
> **Note:** Campus web applications do not necessarily need to pass a\
> transaction ID to uPay; however, without a transaction ID the campus
> organization will likely have difficulty matching payment information
> with customer information. We recommend use of the EXT_TRANS_ID\
> parameter, which allows for payment search on this parameter in the
> Marketplace Operations Center.

+-----------------------------------+-----------------------------------+
| > Posting URL Parameters          | > Once a uPay site has been       |
|                                   | > configured to use a posting     |
|                                   | > URL, transaction parameters     |
|                                   | > will be passed by uPay to the   |
|                                   | > posting URL. The customer's     |
|                                   | > browser is not navigated to the |
|                                   | > posting URL, but the parameters |
|                                   | > are posted to it. The web       |
|                                   | > application targeted by the     |
|                                   | > posting URL must be able to     |
|                                   | > process these parameters. It is |
|                                   | > your responsibility to contact  |
|                                   | > the\                            |
|                                   | > administrator of the campus web |
|                                   | > application and provide that    |
|                                   | > person with information about   |
|                                   | > the posting-URL parameters.     |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

+-----------------------------------------------------------------------+
| > ***Important!*** Technical details on configuring a campus web      |
| > application to accept the parameters passed to a posting URL are    |
| > outside the scope of this document.                                 |
+=======================================================================+
+-----------------------------------------------------------------------+

> The following parameters are posted *along with any other parameters
> that the web application initially passed to uPay, except for
> VALIDATION_KEY*:
>
> **Parameters for both payment card transactions and ACH
> transactions:**

+-----------------+-----------------+-----------------+-----------------+
| >               | **Description** | **Field         | > **Data Type** |
|  **Parameters** |                 | Length**        |                 |
+=================+=================+=================+=================+
+-----------------+-----------------+-----------------+-----------------+

> The Additional Posting Value specified on the\
> uPay Miscellaneous Settings page. Some

+-----------------+-----------------+-----------------+-----------------+
| > posting_key   | campus web      | 30              | alphanumeric    |
|                 | applications    |                 |                 |
|                 | use this value  |                 |                 |
|                 | to              |                 |                 |
+=================+=================+=================+=================+
+-----------------+-----------------+-----------------+-----------------+

> ensure the identity of the uPay site that is\
> communicating with the posting URL.

+-----------------+-----------------+-----------------+-----------------+
| > tpg_trans_id  | A reference     | > unlimited     | > alphanumeric  |
|                 | number assigned |                 |                 |
|                 | by Payment      |                 |                 |
+=================+=================+=================+=================+
|                 | > Gateway.      |                 |                 |
+-----------------+-----------------+-----------------+-----------------+

> CONFIDENTIAL
>
> uPay Technical Guide©2025 TouchNet Information Systems, Inc.


+-------------+-------------+-------------+-------------+-------------+
| 16          | > Chapter 4 | **De        | **Field     | > **Data    |
|             |             | scription** | Length**    | > Type**    |
+=============+=============+=============+=============+=============+
|             | > **P       |             |             |             |
|             | arameters** |             |             |             |
+-------------+-------------+-------------+-------------+-------------+

+-----------------+-----------------+-----------------+-----------------+
| > ses           | > Unique code   | maximum of      | > alphanumeric  |
| sion_identifier | > that          |                 |                 |
|                 | > identifies    |                 |                 |
|                 | > the session.  |                 |                 |
+=================+=================+=================+=================+
|                 |                 | 48              |                 |
+-----------------+-----------------+-----------------+-----------------+

> Status of the transaction as reported by

+-----------------+-----------------+-----------------+-----------------+
| pmt_status      | > Payment       | unlimited       | alphanumeric    |
|                 | > Gateway.      |                 |                 |
|                 | > Either        |                 |                 |
|                 | > \"success\"   |                 |                 |
|                 | > or            |                 |                 |
+=================+=================+=================+=================+
+-----------------+-----------------+-----------------+-----------------+

> \"cancelled\".
>
> Amount of the transaction processed by\
> Payment Gateway. (Maximum value:\
> \$99,999.99.)
>
> *Forrecurring payments:*

+-----------------+-----------------+-----------------+-----------------+
| > pmt_amt       | > During setup, | 8 (including    | > numeric       |
|                 | > the total     |                 |                 |
|                 | > amount of all |                 |                 |
|                 | > recurring     |                 |                 |
+=================+=================+=================+=================+
|                 | > payments is   |                 |                 |
|                 | > passed to the |                 |                 |
|                 | > posting URL   |                 |                 |
|                 | > as the        |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 |                 | 2 characters    |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 | > pmt_amt       |                 |                 |
|                 | > parameter.    |                 |                 |
|                 | > This is the   |                 |                 |
|                 | > same          |                 |                 |
|                 | > parameter     |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 |                 | > after the     |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 | > used for each |                 |                 |
|                 | > recurring     |                 |                 |
|                 | > payment. The  |                 |                 |
|                 | > campus        |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 |                 | > decimal       |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 | > web           |                 |                 |
|                 | > application   |                 |                 |
|                 | > must be able  |                 |                 |
|                 | > to use the    |                 |                 |
|                 | > value         |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 |                 | > point)        |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 | passed to the   |                 |                 |
|                 | posting URL in  |                 |                 |
|                 | the recurring\_ |                 |                 |
+-----------------+-----------------+-----------------+-----------------+

> payment_type parameter (either \"setup\" or\
> \"payment\") to determine if pmt_amt represents\
> a total for all recurring payments or the amount\
> for an individual recurring payment.

+-----------------+-----------------+-----------------+-----------------+
| > pmt_date      | > Date the      | > unlimited     | alphanumeric    |
|                 | > transaction   |                 |                 |
|                 | > was processed |                 |                 |
|                 | > by Payment    |                 |                 |
+=================+=================+=================+=================+
|                 | > Gateway.      |                 |                 |
|                 | > (Format:      |                 |                 |
|                 | > mm/dd/yyyy.)  |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| > name_on_acct  | > Name on       | > 50            | alphanumeric    |
|                 | > payment card  |                 |                 |
|                 | > account or    |                 |                 |
|                 | > bank          |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 | > account.      |                 |                 |
+-----------------+-----------------+-----------------+-----------------+

> The address entered by the customer in uPay.

+-----------------+-----------------+-----------------+-----------------+
| > acct_addr     | > This          | > 35            | alphanumeric    |
|                 | > parameter is  |                 |                 |
|                 | > passed only   |                 |                 |
|                 | > if the uPay   |                 |                 |
|                 | > site          |                 |                 |
+=================+=================+=================+=================+
|                 | > has been set  |                 |                 |
|                 | > up to require |                 |                 |
|                 | > address       |                 |                 |
|                 | > verification  |                 |                 |
+-----------------+-----------------+-----------------+-----------------+

> data.
>
> The second address line entered by the cus-

+-----------------+-----------------+-----------------+-----------------+
| acct_addr2      | > tomer in      | > 35            | alphanumeric    |
|                 | > uPay. This    |                 |                 |
|                 | > parameter is  |                 |                 |
|                 | > passed only   |                 |                 |
|                 | > if            |                 |                 |
+=================+=================+=================+=================+
|                 | > the uPay site |                 |                 |
|                 | > has been set  |                 |                 |
|                 | > up to require |                 |                 |
|                 | > address       |                 |                 |
+-----------------+-----------------+-----------------+-----------------+

> verification data.
>
> The city entered by the customer in uPay. This

+-----------------+-----------------+-----------------+-----------------+
| > acct_city     | > parameter is  | > 35            | alphanumeric    |
|                 | > passed only   |                 |                 |
|                 | > if the uPay   |                 |                 |
|                 | > site has      |                 |                 |
+=================+=================+=================+=================+
+-----------------+-----------------+-----------------+-----------------+

> been set up to require address verification data.
>
> The state entered by the customer in uPay. This

+-----------------+-----------------+-----------------+-----------------+
| > acct_state    | > parameter is  | 2               | alphanumeric    |
|                 | > passed only   |                 |                 |
|                 | > if the uPay   |                 |                 |
|                 | > site has      |                 |                 |
+=================+=================+=================+=================+
+-----------------+-----------------+-----------------+-----------------+

> been set up to require address verification data.
>
> uPay Technical Guide\
> ©2025 TouchNet Information Systems, Inc.

CONFIDENTIAL


+-------------+-------------+-------------+-------------+-------------+
| > 2.0 Using | **De        | **Field     | > **Data    | 17          |
| > a Posting | scription** | Length**    | > Type**    |             |
| > URL       |             |             |             |             |
+=============+=============+=============+=============+=============+
| > **P       |             |             |             |             |
| arameters** |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+

> The zip code entered by the customer in uPay.

+-----------------+-----------------+-----------------+-----------------+
| > acct_zip      | > This          | > 30            | alphanumeric    |
|                 | > parameter is  |                 |                 |
|                 | > passed only   |                 |                 |
|                 | > if the uPay   |                 |                 |
|                 | > site          |                 |                 |
+=================+=================+=================+=================+
|                 | > has been set  |                 |                 |
|                 | > up to require |                 |                 |
|                 | > address       |                 |                 |
|                 | > verification  |                 |                 |
+-----------------+-----------------+-----------------+-----------------+

> data.
>
> The country selected by the customer.
>
> The two-letter code represents the English\
> language country codes approved by the\
> International Organization for Standardization.

+-----------------+-----------------+-----------------+-----------------+
| acct_country    | > This list can | 2               | alphabetic      |
|                 | > be found at   |                 |                 |
+=================+=================+=================+=================+
+-----------------+-----------------+-----------------+-----------------+

> www.iso.org/iso/country_codes.htm.
>
> This parameter is passed only if the uPay site\
> has been set up to require address verification\
> data.

+-----------------+-----------------+-----------------+-----------------+
| > acct_email\_  | > The customer  | > 50            | alphanumeric    |
|                 | > can be        |                 |                 |
|                 | > required to   |                 |                 |
|                 | > enter an e-   |                 |                 |
+=================+=================+=================+=================+
| > address       | > mail address  |                 |                 |
|                 | > or this field |                 |                 |
|                 | > can be        |                 |                 |
|                 | > optional.     |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| acct_phone_day  | > This phone    | > 20            | alphanumeric    |
|                 | > field is an   |                 |                 |
|                 | > optional      |                 |                 |
|                 | > entry field.  |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| > a             | > This phone    | > 20            | alphanumeric    |
| cct_phone_night | > field is an   |                 |                 |
|                 | > optional      |                 |                 |
|                 | > entry field.  |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| > acct_phone\_  | > This phone    | > 20            | alphanumeric    |
|                 | > field is an   |                 |                 |
|                 | > optional      |                 |                 |
|                 | > entry field.  |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| > mobile        |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+

> An ID generated/assigned by your campus web

+-----------------+-----------------+-----------------+-----------------+
| EXT_TRANS_ID    | application.    | > 250           | > alphanumeric  |
|                 | This value is   |                 |                 |
|                 | posted only if  |                 |                 |
|                 | it was          |                 |                 |
+=================+=================+=================+=================+
|                 | initially       |                 |                 |
|                 | passed to uPay  |                 |                 |
|                 | from the campus |                 |                 |
|                 | web             |                 |                 |
+-----------------+-----------------+-----------------+-----------------+

> application.
>
> A unique ID that identifies the uPay site.

+-----------------+-----------------+-----------------+-----------------+
| UPAY_SITE_ID    | Assigned by     | unlimited       | > numeric       |
|                 | Marketplace     |                 |                 |
|                 | when the uPay   |                 |                 |
|                 | site            |                 |                 |
+=================+=================+=================+=================+
+-----------------+-----------------+-----------------+-----------------+

> was created.
>
> An internal Marketplace identifier (also known

+-----------------+-----------------+-----------------+-----------------+
| sys_tracking_id | > as the order  | unlimited       | > numeric       |
|                 | > ID) that is   |                 |                 |
|                 | > displayed to  |                 |                 |
|                 | > the           |                 |                 |
+=================+=================+=================+=================+
+-----------------+-----------------+-----------------+-----------------+

> customer on the uPay receipt page.
>
> CONFIDENTIAL
>
> uPay Technical Guide©2025 TouchNet Information Systems, Inc.


+-------------+-------------+-------------+-------------+-------------+
| 18          | > Chapter 4 | **De        | **Field     | > **Data    |
|             |             | scription** | Length**    | > Type**    |
+=============+=============+=============+=============+=============+
|             | > **P       |             |             |             |
|             | arameters** |             |             |             |
+-------------+-------------+-------------+-------------+-------------+

> This value is only specified if the payment is a\
> recurring payment. Two values are possible:\
> \"setup\" (for the initial setup of recurring\
> payments) and \"payment\" (for a single recurring\
> payment).
>
> During setup, the total amount of all scheduled

+-----------------+-----------------+-----------------+-----------------+
| > recurring\_   | payments is     | > unlimited     | alphanumeric    |
|                 | passed to the   |                 |                 |
|                 | posting URL as  |                 |                 |
|                 | the             |                 |                 |
+=================+=================+=================+=================+
|                 | > pmt_amt       |                 |                 |
|                 | > parameter.    |                 |                 |
|                 | > This is the   |                 |                 |
|                 | > same          |                 |                 |
|                 | > parameter     |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| > payment_type  |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 | used for each   |                 |                 |
|                 | recurring       |                 |                 |
|                 | payment. The    |                 |                 |
|                 | campus          |                 |                 |
+-----------------+-----------------+-----------------+-----------------+

> web application must be able to use the value\
> passed to the posting URL in the recurring\_\
> payment_type parameter (either \"setup\" or\
> \"payment\") to determine if pmt_amt represents\
> a total for all recurring payments or the amount\
> for an individual recurring payment.

+-----------------+-----------------+-----------------+-----------------+
| > re            | > This value is | > unlimited     | > numeric       |
| curring_setup\_ | > specified for |                 |                 |
|                 | > uPay-driven   |                 |                 |
|                 | > recurring     |                 |                 |
+=================+=================+=================+=================+
| > number_of\_   | > payments and  |                 |                 |
|                 | > indicates the |                 |                 |
|                 | > total number  |                 |                 |
|                 | > of            |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| > payments      | > payments.     | > 10            | alphanumeric    |
+-----------------+-----------------+-----------------+-----------------+
|                 | > This value is |                 |                 |
|                 | > specified for |                 |                 |
|                 | > uPay-driven   |                 |                 |
|                 | > recurring     |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| > re            |                 |                 |                 |
| curring_setup\_ |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 | > payments and  |                 |                 |
|                 | > indicates the |                 |                 |
|                 | > date of the   |                 |                 |
|                 | > first         |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| > start_date    |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 | > scheduled     |                 |                 |
|                 | > payment.      |                 |                 |
|                 | > (Format:      |                 |                 |
|                 | > mm/dd/yyyy.)  |                 |                 |
+-----------------+-----------------+-----------------+-----------------+

> This value is specified for uPay-driven recurring\
> payments and indicates the date when the\
> recurring payments will end. If this date does

+-----------------+-----------------+-----------------+-----------------+
| > re            | > not coincide  | > 10            | alphanumeric    |
| curring_setup\_ | > with a        |                 |                 |
|                 | > scheduled     |                 |                 |
|                 | > payment date  |                 |                 |
|                 | > (as           |                 |                 |
+=================+=================+=================+=================+
|                 | determined by   |                 |                 |
|                 | the selected    |                 |                 |
|                 | frequency and   |                 |                 |
|                 | start           |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| > end_date      |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 | > date), the    |                 |                 |
|                 | > final payment |                 |                 |
|                 | > will be the   |                 |                 |
|                 | > last          |                 |                 |
+-----------------+-----------------+-----------------+-----------------+

> regularly scheduled payment date before the\
> \"recurring_setup_end_date\". (Format:\
> mm/dd/yyyy.)
>
> This numerical value is specified for uPay-

+-----------------+-----------------+-----------------+-----------------+
| > re            | driven          | unlimited       | > numeric       |
| curring_setup\_ | recurring       |                 |                 |
|                 | payments and    |                 |                 |
|                 | indicates the   |                 |                 |
+=================+=================+=================+=================+
|                 | > frequency of  |                 |                 |
|                 | > payments:     |                 |                 |
|                 | > 4=weekly,     |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| > frequency     |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 | > 1=monthly,    |                 |                 |
|                 | > 2=bi-monthly, |                 |                 |
|                 | > 5=quarterly,  |                 |                 |
+-----------------+-----------------+-----------------+-----------------+

> 6=semi-annually, and 7=annually.
>
> **Additional parameters for payment card transactions:**

+-----------------+-----------------+-----------------+-----------------+
| **Parameters**  | **Description** | **Field         | **Data Type**   |
|                 |                 | Length**        |                 |
+=================+=================+=================+=================+
| > card_type     | > Type of       | unlimited       | > alphanumeric  |
|                 | > payment card: |                 |                 |
|                 | > Mastercard,   |                 |                 |
|                 | > Visa,         |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 | > American      |                 |                 |
|                 | > Express,      |                 |                 |
|                 | > Discover,     |                 |                 |
|                 | > etc.          |                 |                 |
+-----------------+-----------------+-----------------+-----------------+

> uPay Technical Guide\
> ©2025 TouchNet Information Systems, Inc.

CONFIDENTIAL


+-----------------------------------+-----------------------------------+
| > 2.0 Using a Posting URL         | 19                                |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> **Additional parameters for ACH transactions:**

+-----------------+-----------------+-----------------+-----------------+
| **Parameters**  | **Description** | > **Field       | > **Data Type** |
|                 |                 | > Length**      |                 |
+=================+=================+=================+=================+
| > bank_name     | > These values  | > unlimited     | > alphanumeric  |
|                 | > are obtained  |                 |                 |
|                 | > from Payment  |                 |                 |
|                 | > Gate-         |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 | > way based on  |                 |                 |
|                 | > the routing   |                 |                 |
|                 | > number        |                 |                 |
|                 | > entered       |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| > bank_addr1    | > These values  | > unlimited     | > alphanumeric  |
|                 | > are obtained  |                 |                 |
|                 | > from Payment  |                 |                 |
|                 | > Gate-         |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 | > way based on  |                 |                 |
|                 | > the routing   |                 |                 |
|                 | > number        |                 |                 |
|                 | > entered       |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| > bank_addr2    | > These values  | > unlimited     | > alphanumeric  |
|                 | > are obtained  |                 |                 |
|                 | > from Payment  |                 |                 |
|                 | > Gate-         |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 | > way based on  |                 |                 |
|                 | > the routing   |                 |                 |
|                 | > number        |                 |                 |
|                 | > entered       |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| bank_routing\_  | > These values  | > unlimited     | > alphanumeric  |
|                 | > are obtained  |                 |                 |
|                 | > from Payment  |                 |                 |
|                 | > Gate-         |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| > num           | > way based on  |                 |                 |
|                 | > the routing   |                 |                 |
|                 | > number        |                 |                 |
|                 | > entered       |                 |                 |
+-----------------+-----------------+-----------------+-----------------+

> **Additional parameter for PayPath transactions:**

+-----------------+-----------------+-----------------+-----------------+
| **Parameters**  | **Description** | > **Field       | > **Data Type** |
|                 |                 | > Length**      |                 |
+=================+=================+=================+=================+
| > PAYPATH\_     | A reference     | > unlimited     | > alphanumeric  |
|                 | number that     |                 |                 |
|                 | identifies the  |                 |                 |
|                 | PayPath         |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| > TRANSACTION\_ |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 | > transaction.  |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| > ID            |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+

**Parameters for cancellations:**

+-----------------+-----------------+-----------------+-----------------+
| **Parameters**  | **Description** | > **Field       | > **Data Type** |
|                 |                 | > Length**      |                 |
+=================+=================+=================+=================+
| > posting_key   | A security      | > unlimited     | > alphanumeric  |
|                 | value specified |                 |                 |
|                 | when the uPay   |                 |                 |
|                 | site            |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 | > was built.    |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| > pmt_status    | > This value is | > unlimited     | > alphanumeric  |
|                 | > always        |                 |                 |
|                 | > \"cancelled\" |                 |                 |
|                 | > for           |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 | >               |                 |                 |
|                 |  cancellations. |                 |                 |
+-----------------+-----------------+-----------------+-----------------+

> A unique ID generated/assigned by your

+-----------------+-----------------+-----------------+-----------------+
| EXT_TRANS_ID    | campus web      | > 250           | > alphanumeric  |
|                 | application.    |                 |                 |
|                 | This value is   |                 |                 |
|                 | posted          |                 |                 |
+=================+=================+=================+=================+
|                 | only if it was  |                 |                 |
|                 | initially       |                 |                 |
|                 | passed to uPay  |                 |                 |
|                 | from the        |                 |                 |
+-----------------+-----------------+-----------------+-----------------+

> campus web application.

+-------------+-------------+-------------+-------------+-------------+
| U           |             | > A unique  | unlimited   | > numeric   |
| PAY_SITE_ID |             | > ID that   |             |             |
|             |             | >           |             |             |
|             |             |  identifies |             |             |
|             |             | > the uPay  |             |             |
|             |             | > site.     |             |             |
+=============+=============+=============+=============+=============+
|             |             | > Assigned  |             |             |
|             |             | > when the  |             |             |
|             |             | > uPay site |             |             |
|             |             | > was       |             |             |
|             |             | > created.  |             |             |
+-------------+-------------+-------------+-------------+-------------+
| > 2.1       | > About     |             |             |             |
|             | > Recurring |             |             |             |
|             | > Payment   |             |             |             |
|             | >           |             |             |             |
|             |  Parameters |             |             |             |
+-------------+-------------+-------------+-------------+-------------+

> For recurring payments, the following parameters are passed when
> recurring payments are established and for each subsequent recurring
> payment that is processed:\
> ▪ sys_tracking_id\
> ▪ posting_key
>
> CONFIDENTIAL
>
> uPay Technical Guide©2025 TouchNet Information Systems, Inc.

+-----------------+-----------------+-----------------+-----------------+
| 20              | > Chapter 4     | ▪               | > name_on_acct  |
+=================+=================+=================+=================+
|                 |                 | ▪               | > acct_addr     |
+-----------------+-----------------+-----------------+-----------------+
|                 |                 | ▪               | > acct_addr2    |
+-----------------+-----------------+-----------------+-----------------+
|                 |                 | ▪               | > acct_city     |
+-----------------+-----------------+-----------------+-----------------+
|                 |                 | ▪               | > acct_state    |
+-----------------+-----------------+-----------------+-----------------+
|                 |                 | ▪               | > acct_zip      |
+-----------------+-----------------+-----------------+-----------------+
|                 |                 | ▪               | > acct_country  |
+-----------------+-----------------+-----------------+-----------------+
|                 |                 | ▪               | > acc           |
|                 |                 |                 | t_email_address |
+-----------------+-----------------+-----------------+-----------------+
|                 |                 | ▪               | >               |
|                 |                 |                 |  acct_phone_day |
+-----------------+-----------------+-----------------+-----------------+
|                 |                 | ▪               | > a             |
|                 |                 |                 | cct_phone_night |
+-----------------+-----------------+-----------------+-----------------+
|                 |                 | ▪               | > ac            |
|                 |                 |                 | ct_phone_mobile |
+-----------------+-----------------+-----------------+-----------------+
|                 |                 | ▪               | > UPAY_SITE_ID  |
+-----------------+-----------------+-----------------+-----------------+
|                 |                 | ▪               | > card_type     |
+-----------------+-----------------+-----------------+-----------------+
|                 |                 | ▪               | > pmt_amt       |
+-----------------+-----------------+-----------------+-----------------+
|                 |                 | ▪               | > recurri       |
|                 |                 |                 | ng_payment_type |
+-----------------+-----------------+-----------------+-----------------+
|                 |                 | ▪               | > recu          |
|                 |                 |                 | rring_setup_num |
|                 |                 |                 | ber_of_payments |
+-----------------+-----------------+-----------------+-----------------+
|                 |                 | ▪               | > recurring_s   |
|                 |                 |                 | etup_start_date |
+-----------------+-----------------+-----------------+-----------------+
|                 |                 | ▪               | > recurring     |
|                 |                 |                 | _setup_end_date |
+-----------------+-----------------+-----------------+-----------------+
|                 |                 | ▪               | > recurring_    |
|                 |                 |                 | setup_frequency |
+-----------------+-----------------+-----------------+-----------------+

And the following additional parameters are passed for each recurring

payment that is processed (and not when the recurring payments are

established):

> ▪ pmt_status
>
> ▪ pmt_date
>
> ▪ tpg_trans_id
>
> uPay Technical Guide\
> ©2025 TouchNet Information Systems, Inc.

CONFIDENTIAL

+-----------------------+-----------------------+-----------------------+
| > 3.0 Passing         |                       | 21                    |
| > Accounting Codes to |                       |                       |
| > uPay                |                       |                       |
+=======================+=======================+=======================+
| > 3.0                 | > Passing Accounting  |                       |
|                       | > Codes to uPay       |                       |
+-----------------------+-----------------------+-----------------------+

*Banner*

> If you would like to pass accounting codes to your uPay site, you must
> pass a Banner Detail Code.
>
> If you don\'t know what value to enter, contact your Banner
> administrator for a list of the Detail Codes.
>
> The value that you enter is not validated by uPay or Payment Gateway,
> so you must make sure you enter a valid value.
>
> **Note:** If you enter an incomplete or incorrect value for a passed
> accounting code, the transaction will still be accepted (provided the
> customer enters valid payment information); however, a GL exception
> will be generated. A uPay site manager should resolve any GL
> exceptions that result.

*Colleague*

> If you would like to pass accounting codes to your uPay site, you must
> pass a Colleague account number (or Colleague NARD shortcut code).
>
> If you don\'t know what value to enter, contact your Colleague
> administrator for a list of the Colleague account numbers (or NARD
> codes).
>
> The value that you enter is not validated by uPay or Payment Gateway,
> so you must make sure you enter a valid value.
>
> **Note:** If you enter an incomplete or incorrect value for a passed
> accounting code, the transaction will still be accepted (provided the
> customer enters valid payment information); however, a GL exception
> will be generated. A uPay site manager should resolve any GL
> exceptions that result.

*Peoplesoft*

> If you would like to pass accounting codes to your uPay site, as
> described in \"Passing Parameters to Your uPay Site\" on page 530, you
> must pass a combination of the applicable PeopleSoft Business Unit and
> SpeedType.

This information must be entered in this format:

\[Business Unit\]\^\[SpeedType\]

> For example, if the Business Unit is 0001 and the SpeedType is
> 11_01_01\_ 00_00000_41012, then you would enter
> 0001\^11_01_01_00_00000\_ 41012.
>
> If you don\'t know what value to enter, contact your
> PeopleSoftadministrator for a list of the Business Units and
> SpeedTypes.
>
> CONFIDENTIAL
>
> uPay Technical Guide©2025 TouchNet Information Systems, Inc.

+-----------------------------------+-----------------------------------+
| 22                                | > Chapter 4                       |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> The value that you enter is not validated by uPay or Payment Gateway,
> so you must make sure you enter a valid value.
>
> **Note:** If you enter an incomplete or incorrect value for a passed
> accounting code, the transaction will still be accepted (provided the
> customer enters valid payment information); however, a GL exception
> will be generated. A uPay site manager should resolve any GL
> exceptions that result.

*Workday*

> You can pass parameters from a campus web application to your uPay
> site. For the CREDIT_ACCT_CODE parameter, you must pass a Ledger ID
> and all applicable Worktags and their values. You must pass these
> values with valid XML. CREDIT_ACCT_AMT must also be passed.

+-----------------------------------------------------------------------+
| > ***Important!*** When you pass the CREDIT_ACCT_CODE parameter, none |
| > of the values associated with the uPay site\'s assigned Marketplace |
| > accounting code will be used, so you must ensure that you send a    |
| > complete set of Workday general ledger data.                        |
+=======================================================================+
+-----------------------------------------------------------------------+

> Additional sets of data may be sent with CREDIT_ACCT_CODE\_#\
> (example: CREDIT_ACCT_CODE_2). Whenever CREDIT_ACCT_CODE\_# is passed,
> a corresponding CREDIT_ACCT_AMT\_# must be passed to specify the
> amount. Any additional credit accounting codes passed must be in
> numerical sequence (i.e., don\'t skip any numbers). There is no limit
> to the number of credit accounting codes that can be passed as input
> parameters.
>
> Here is an example of XML passed for the CREDIT_ACCT_CODE field:
> \<ACCOUNT_INFO\>\
> \<LEDGER id=\"54000\"\>\
> \<PARENT /\>\
> \</LEDGER\>\
> \<SPEND_CATEGORY /\>\
> \<REVENUE_CATEGORY /\>\
> \<WORKTAG type=\"Spend_Category_ID\"\>Spend_Cat_Office\_
> Supplies\</WORKTAG\>\
> \<WORKTAG type=\"Business_Unit_ID\"\>42\</WORKTAG\> \<WORKTAG
> type=\"Cost_Center_Reference_ID\"\>CC\_\
> 43010\</WORKTAG\>\
> \<WORKTAG type=\"Catalog_Item_ID\" /\>\
> \<WORKTAG type=\"Job_Level_ID\" /\>\
> \<WORKTAG type=\"Gift_Reference_ID\"\>00000\</WORKTAG\> \<WORKTAG
> type=\"Fund_ID\"\>10\</WORKTAG\>\
> \</ACCOUNT_INFO\>
>
> uPay Technical Guide\
> ©2025 TouchNet Information Systems, Inc.

CONFIDENTIAL

+-----------------------------------+-----------------------------------+
| > 3.0 Passing Accounting Codes to | 23                                |
| > uPay                            |                                   |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

The following rules must be followed when passing XML for the CREDIT\_

ACCT_CODE parameter:

> ● The entire set of XML must be wrapped with \<ACCOUNT_INFO\>

and \</ACCOUNT_INFO\>

> ● The XML can be one string or multiple lines.
>
> ● Any number of WORKTAG fields can be passed, but the name of the

Worktag must be specified in the \"type\" field and the value must be

specified between the open and close WORKTAG tags.

> ● A value for LEDGER must be passed in the \"id\" field or a GL

exception will occur.

> ● Values for SPEND_CATEGORY and REVENUE_CATEGORY may

optionally be passed. The values for these tags must be passed

between the corresponding open and close tags.

> ● The passed XML must not exceed 2000 total characters.

If you do not know what values to enter, be sure to contact your Workday

administrator.

The value that you enter is not validated by uPay, so you must make sure

you enter valid Workday values.

**Note:** If the campus web application passes an incomplete or
incorrect

value for the CREDIT_ACCT_CODE parameter, the transaction will still be

accepted (provided the customer enters valid payment information);

however, a GL exception will be generated. A uPay site manager should

resolve any GL exceptions that result.

+-----------------------------------------------------------------------+
| > ***Important!*** The DEBIT_ACCT_CODE parameter cannot be passed to  |
| > uPay when Workday general ledger integration is used. uPay sites    |
| > will always pass the value configured in the uPay site\'s \"Bank    |
| > Account ID\" field when reporting a value for                       |
| > Bank_Account_Reference to Workday.                                  |
+=======================================================================+
+-----------------------------------------------------------------------+

> CONFIDENTIAL
>
> uPay Technical Guide©2025 TouchNet Information Systems, Inc.

+-----------------------------------+-----------------------------------+
| 24                                | > Chapter 4                       |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> uPay Technical Guide\
> ©2025 TouchNet Information Systems, Inc.

CONFIDENTIAL
