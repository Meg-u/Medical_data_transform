--models/dim_products.sql
select distinct lower(trim(product)) as product_name
  from
   {
      {
         ref('fct_messages')
      }
   }
 where product is not null:
   and product != ''
   
   