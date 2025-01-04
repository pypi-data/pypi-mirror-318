insert into {{ model.get_fqtn(ctx) }} ({{columns | join(', ')}})
values ({% for c in columns %} %({{c}})s{% if not loop.last %},{% endif %}{% endfor %})
returning {{pk_col}};
