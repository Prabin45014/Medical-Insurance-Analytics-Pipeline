select
    region,
    avg(annual_medical_cost) as avg_medical_cost,
    avg(annual_premium) as avg_premium,
    sum(total_claims_paid) as total_claims_paid,
    count(distinct person_id) as customer_count
from {{ ref('stg_medical_insurance') }}
group by region
