select
    person_id,
    cast(age as int64) as age,
    lower(sex) as sex,
    lower(region) as region,
    urban_rural,
    bmi,
    smoker,
    hypertension,
    diabetes,
    annual_medical_cost,
    annual_premium,
    claims_count,
    total_claims_paid,
    risk_score,
    is_high_risk
from {{ source('insurance_raw', 'medical_insurance_raw') }}
