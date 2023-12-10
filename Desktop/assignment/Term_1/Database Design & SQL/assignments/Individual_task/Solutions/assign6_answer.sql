--List all criminal aliases beginning with the letter B.
SELECT alias_id, criminal_id, alias
FROM aliases
WHERE alias LIKE 'B%'

--List all crimes that occurred (were charged) during the month November 2008. List the crime ID, criminal ID, date charged, and classification.
SELECT crime_id AS roshan_Crime_ID, criminal_id, date_charged, classification
FROM crimes
WHERE EXTRACT(MONTH FROM date_charged) = 11 AND EXTRACT(YEAR FROM date_charged) = 2008


--List all crimes with a status of CA (can appeal) or IA (in appeal). List the crime ID, criminal ID, date charged, and status.
SELECT crime_id AS roshan_Crime_ID, criminal_id, date_charged, status
FROM crimes
WHERE status IN ('CA', 'IA')

--List all crimes classified as a felony. List the crime ID, criminal ID, date charged, and classification. (classification is ‘F’).
SELECT crime_id AS roshan_Crime_ID, criminal_id, date_charged, classification
FROM crimes
WHERE classification = 'F'

--List all crimes with a hearing date more than 14 days after the date charged. List the crime ID, criminal ID, date charged, and hearing date.
SELECT crime_id AS roshan_Crime_ID, criminal_id, date_charged, hearing_date
FROM crimes
WHERE hearing_date > date_charged + 14

-- List all criminals with the zip code 23510. List the criminal ID, last name, and zip code. Sortthe list by criminal ID.
SELECT criminal_id AS roshan_Criminal_ID, last, zip
FROM criminals
WHERE zip = '23510'
ORDER BY criminal_id


--List all crimes that don’t have a hearing date scheduled. List the crime ID, criminal ID, date charged, and hearing date.
SELECT crime_id AS roshan_Crime_ID, criminal_id, date_charged, hearing_date
FROM crimes
WHERE hearing_date IS NULL

--List all sentences with a probation officer assigned. List the sentence ID, criminal ID, and probation officer ID. Sort the list by probation officer ID and then criminal ID.
SELECT sentence_id AS roshan_Sentence_ID, criminal_id, prob_id
FROM sentences
WHERE prob_id IS NOT NULL
ORDER BY prob_id, criminal_id

---List all crimes that are classified as misdemeanors (classification =’M’) and are currently in appeal (stat is ‘IA’). List the crime ID, criminal ID, classification, and status.
SELECT crime_id AS roshan_Crime_ID, criminal_id, classification, status
FROM crimes
WHERE classification = 'M' AND status = 'IA'

--List all crime charges with a balance owed. List the charge ID, crime ID, fine amount, court fee, amount paid, and amount owed.
SELECT charge_id AS roshan_Charge_ID, crime_id, fine_amount, court_fee, amount_paid, (fine_amount + court_fee - amount_paid) AS amount_owed
FROM crime_charges
WHERE (fine_amount + court_fee - amount_paid) > 0

