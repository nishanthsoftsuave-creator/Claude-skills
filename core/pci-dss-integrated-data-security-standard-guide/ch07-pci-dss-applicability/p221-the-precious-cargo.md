---
title: "The Precious Cargo"
book: pci-dss-integrated-data-security-standard-guide
chapter: 7
source_pages: "221-229"
format: source-text
---
# The Precious Cargo
(Source: PDF pp. 221-229)

<!-- PDF p. 221 (book p. 198) -->

It is extremely helpful to treat your payment card as precious cargo and to understand what contributes to payment card data and to be able to differentiate between the two categories of payment data types (Category 1 and Category 2).

The following sections aim to deconstruct the content of a payment card, so that you will better understand how the payment card data is pieced together. This will give you a greater understanding on why the criminals seek any opportunity to gain unauthorized access to any pieces of payment card data so that they can then gather these together to reconstruct them into a single valid payment card.

<!-- PDF p. 222 (book p. 199) -->

*[Figure omitted]*

**Figure 7-5.** *Payment Card Overview*

## Precious Cargo Categories

The two categories of data types are as follows:

- The “long number” for the card *(typically, 15 or 16 digits in length)*, which is referred to as the Primary Account Number (PAN)
- The Sensitive Authentication Data (SAD)

Precious Cargo

Category 1:

Cardholder Data (CHD)

Category 2:

Sensitive Authentication Data (SAD)

- paN
- Cardholder Name
- expiration Date
- Service Code
  - Full track data (magnetic stripe or equivalent chip data)
  - CaV2/CVC2/CVV2/CID
  - pINs/pIN blocks

## Structure of a Payment Card

<!-- PDF p. 223 (book p. 200) -->

### Front of Payment Card Breakdown

The front of the payment card is commonly where you will find the category 1 datasets. However, there are some card issuers that have started to locate the category 1 data on the rear of the payment card. An example of the front of the card can be seen in Figure 7- 5 and consists of the following components.

Primary Account Number (PAN)

When looking at the full bank card number, the first digit identifies the card issuer’s industry, while the first six digits collectively identify the specific institution which issued the card. The remainder of the 16 (or 15, in some cases) digits make up the cardholder’s account number, including one or more check digits, also called a “checksum.” A checksum represents the sum of a formula that helps determine if the credit card number is actually valid.

*[Figure omitted]*

Major Identifier No. (MII) The MII identifies the category or type of institution which issued the card. Visa- and Mastercard-branded cards.

MII Digit Value Issuer Category

0 ISO/tC 68 assignment

1 airline cards

2 airlines cards (and other future industry assignments)

3 travel and entertainment Cards

4 banking and Financial Cards

5 banking and Financial Cards

6 Merchandising and Financial Cards

7 Gas Cards, Other Future Industry assignments

(*continued*)

<!-- PDF p. 224 (book p. 201) -->

8 healthcare Cards, telecommunications, Other Future Industry assignments

9 For Use by National Standards bodies

*[Figure omitted]*

Issuer Identification No. The IIN provides merchants with a lot of other information besides just the issuing entity. For example, when a cardholder enters their card details for an online transaction, just these first few digits tell the retailer:

- The name, address, and phone number of the bank funds will be transferred from
- The card brand (Visa, Mastercard, American Express, etc.)
- What type of card it is (debit, credit, prepaid, etc.)?
- What level the card is (black, platinum, business)?
- Whether the issuer is in the same country as the device used in the transaction.
- Whether the address provided by the cardholder matches the one on file.
- Finally, the IIN allows merchants to accept multiple forms of payment and speed up the overall processing.

(*continued*)

<!-- PDF p. 225 (book p. 202) -->

examples of the IIN format for the most widely used card brands

Visa 4****

MasterCard 51**** or 55****

American Express (AMEX) 34**** or 37****

Discover Card 6011, 622126-622925, 644- 649, 65

JCB 3528–3589

*[Figure omitted]*

account No. associated with payment card

The following 6–9 digits represent a unique bank account number. (Note: The bank account number of a customer but the account number assigned to a credit account).

*[Figure omitted]*

Checksum This digit is mathematically determined based on all the other digits and is used to minimize the risk associated with human error, when manually inputting the “long card number.” This enables a checksum verification using the Luhn algorithm (MOD-10 mathematics). Using the checksum against the IS Centurion payment card, shown earlier, confirms that this is not a valid “long number.”

*[Figure omitted]*

(*continued*)

<!-- PDF p. 226 (book p. 203) -->

- to calculate the check digit
  - Multiply every even-position digit (when counted from the right) in the number by two. If the result is a two-digit number, then add these digits together to make a single digit (this is called the digital root).
  - to this total, we then add every odd-position digit.
- this will result in a total (in our example =67).
  - the check digit is what number needs to be added to this total to make the next multiple of 10. In this case, 3 will need to be added to make 70.
- the correct check digit for this fictitious number is 3.

Not 2, as seen in Figure 7-5.

*[Figure omitted]*

*[Figure omitted]*

Cardholder Name The person to whom the card has been issued expiration Date typically, 3–4 years from the date of issue (Note: Upon renewal of a payment card, the PAN may remain the same.)

### Rear of Payment Card Breakdown

Commonly, card issuers will locate the magnetic stripe on the rear of the payment card, along with the signature strip and CVV *(except for American Express cards, where the CVV are the four digits located on the front of the payment card).*

Figure 7-6 shows the breakdown of the category 1 and 2 data types contained within the magnetic stripe.

<!-- PDF p. 227 (book p. 204) -->

*[Figure omitted]*

**Figure 7-6.** *Track 1–Track 2 Data*

| Service Code | Three- or four-digit value in the magnetic stripe that follows the expiration date of the payment card on the track data. It is used for various things such as defining service attributes, differentiating between international and national interchange, or identifying usage restrictions. |
|---|---|
| Full track data | As shown in Figure 7-6, the full track data is divided into track 1 and track<br>2, with the storage of track 2 (post authorization) being prohibited, as this contains the SAD relating to the payment card.<br>• Up to 79 characters |

<!-- PDF p. 228 (book p. 205) -->

Security Code The Card Verification Code (CVC) is the three- or four-digit “Security Code” (sometimes referred to as the Card Verification Value (CVV) or Card Identification Number (CID)[^1]):

CAV2 Card Authentication Value 2 (JCB payment cards)

CAV2 Mastercard

CID American Express

CID2 Discover

CVV2 Visa

These are generated by a CVV algorithm and are used to authenticate payment cards. To generate or calculate the three-digit CVV, the algorithm requires the following:

- Primary Account Number (PAN)
- Four-digit Expiration Date
- A pair of Data Encryption Standard (DES keys) (Code Verification Keys (CVKs))
- Three-digit Service Code

Note: This algorithm is only known to the bank and not for any person or organization.

Consequently, because of the aggregated value, it is only permitted for issuers and their supporting companies to store SAD but only if

- There is a justified reason for doing so
- The SAD is stored securely

[^1]: Note: On some payment cards, these can be three or five digits and can be located on the front of the card.

### Personal Identification Number (PIN)/PIN Blocks

If an organization fails to protect their consumers’ PIN/PIN blocks, they are gifting the criminals the keys associated with any stolen payment card details. Suddenly, the criminals have the “free reign” to clone payment cards and to go on a spending spree, using the credit of the affected consumers.

<!-- PDF p. 229 (book p. 206) -->

*[Figure omitted]*

### CHD Storage

The storage of CHD is permitted; however, it is recommended that the Keep It Simple Solution is applied:

“In general, no payment card data should ever be stored unless it’s necessary to meet the needs of the business.

Avoid the unnecessary storage, if this can be avoided, and keep all storage to the absolute minimum needed.

Once the CHD is no longer needed, securely dispose of the CHD.”

“PCI DSS does not prevent a business to store category 1 payment card data.

However, PCI DSS is the de facto security benchmark for the protection of cardholder data and must be applied to the various payment card data lifecycles.”
