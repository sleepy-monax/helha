# Solutions

17.
```sql
SELECT vol.indcomp, COUNT(vol.numvol) as 'tot' from vol WHERE vol.indcomp in ('SWS', 'SNB');
```

# Ressources

- https://sql.sh/cours/group-by
