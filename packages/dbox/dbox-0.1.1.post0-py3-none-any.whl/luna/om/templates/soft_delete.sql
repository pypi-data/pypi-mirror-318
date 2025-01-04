UPDATE {{ model.get_fqtn(ctx) }}
SET deleted_at = NOW();
WHERE
  {{ model.pk_col() }} = %(pk)s
