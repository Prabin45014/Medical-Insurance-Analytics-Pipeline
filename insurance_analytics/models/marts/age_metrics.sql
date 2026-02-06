select
    case
        when age < 30 then 'under_30'
        when age between 30 and 50 then '30_50'
        else '50_plus'
    end as age_group,
    avg(annual_medical_cost) as avg_medical_cost,
    count(distinct person_id) as customer_count
from {{ ref('stg_medical_insurance') }}
group by age_group
