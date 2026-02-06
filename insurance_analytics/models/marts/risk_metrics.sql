select
    is_high_risk,
    count(distinct person_id) as customer_count,
    avg(annual_medical_cost) as avg_medical_cost,
    sum(total_claims_paid) as total_claims_paid
from {{ ref('stg_medical_insurance') }}
group by is_high_risk
