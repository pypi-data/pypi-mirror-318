select *
from {{ input_block.sql_target(ctx) }}
{% if order_by %}
order by {{ order_by | join(', ') }}
{% endif %}
{% if limit %}
limit {{ limit }}
{% endif %}
{% if offset %}
offset {{ offset }}
{% endif %}
