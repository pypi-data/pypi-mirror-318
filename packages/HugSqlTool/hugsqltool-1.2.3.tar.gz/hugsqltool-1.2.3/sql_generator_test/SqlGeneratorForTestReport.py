# encoding=utf-8

import os, re

def generator_sql_switcher(sql_keys:dict)->str:
    generator={ ## 字典存储函数，用作分支处理时更加方便。
    'generator_table_data_rows':generator_table_data_rows,
    'generator_dependencies_incremental_data_row_count':generator_dependencies_incremental_data_row_count,
    'generator_primary_key_check':generator_primary_key_check,
    'generator_dependencies_null_value_ratio_check':generator_dependencies_null_value_ratio_check,
    'generator_dependencies_monitor_of_enumerate_distribution':generator_dependencies_monitor_of_enumerate_distribution,
    'generator_dependencies_json_format_check':generator_dependencies_json_format_check,
    'generator_dependencies_time_format_check':generator_dependencies_time_format_check,
    'generator_dependencies_number_format_check':generator_dependencies_number_format_check,
    'generator_mutil_tab_join_miss_ratio':generator_mutil_tab_join_miss_ratio,
    'generator_mutil_tab_join_rows':generator_mutil_tab_join_rows,
    'generator_idempotence_of_sorting':generator_idempotence_of_sorting,
    'generator_deliverables_data_row_count':generator_deliverables_data_row_count,
    'generator_deliverables_primary_keys_test':generator_deliverables_primary_keys_test,
    'generator_deliverables_null_value_ratio':generator_deliverables_null_value_ratio,
    'generator_deliverables_monitor_of_enumerate_distribution':generator_deliverables_monitor_of_enumerate_distribution,
    'generator_deliverables_json_format_check':generator_deliverables_json_format_check,
    'generator_deliverables_time_format_check':generator_deliverables_time_format_check,
    'generator_deliverables_number_format_check':generator_deliverables_number_format_check,
    'generator_white_namelist_check':generator_white_namelist_check,
    'generator_twin_dataset_rows_check':generator_twin_dataset_rows_check,
    'generator_data_dif_check':generator_data_dif_check
}
    
    test_sql_type=sql_keys.get('test_sql_type','')
    sql_keys.pop('test_sql_type')## sql_keys中其他参数会用作生成SQL，为避免异常问题，去除后续不再使用的test_sql_type键值

    if test_sql_type not in generator:
        return "don't have this generator, plase check."
    else:
        return generator.get(test_sql_type,'')(sql_keys)

def generator_table_data_rows(conf_dict:dict) -> str:
# 输入 conf_dict:{dep_dbtab:"";part_name:"";part_var:"";sys_rows:""}
# 输出 测试SQL生成-离线/dts同步完整性
    sql_content='''---- welcome hugsql ----\n\n
select 
  if(count(1)={{sys_rows}},true,false) 
from {{dep_dbtab}}
where {{part_name}}='{{part_var}}' 

\n---- welcome hugsql ----
'''
    for key,value in conf_dict.items():
        regex = r'({{[ ]*%s[ ]*}})'%(key)
        sql_content= re.sub(regex, value, sql_content)

    return sql_content

def generator_dependencies_incremental_data_row_count(conf_dict:dict) -> str:
# 输入 conf_dict:{dep_dbtab:"";part_name:"";part_var:""}
# 输出 测试SQL生成-增量数据量级
    sql_content='''---- welcome hugsql ----\n\n
select 
  {{part_name}}
  ,count(1) as row_cnt 
from {{dep_dbtab}} 
where {{part_name}}>='{{part_var}}' 
group by 1 
order by {{part_name}} desc
\n\n---- welcome hugsql ----'''
    for key,value in conf_dict.items():
        regex = r'({{[ ]*%s[ ]*}})'%(key)
        sql_content= re.sub(regex, value, sql_content)

    return sql_content

def generator_primary_key_check(conf_dict:dict) -> str:
# 输入 conf_dict:{dep_dbtab:"";part_name:"";part_var:"";fields_code-0:'',fields_code-1:''}
# 输出 测试SQL生成-唯一组合键验证
    sql_content='''---- welcome hugsql ----\n\n
select 
    count(distinct 
    concat(
        {{pk}}
        ) as pk_cnt
    ,count(*) as row_cnt
  from {{dep_dbtab}}
  where {{part_name}}='{{part_var}}'
\n\n---- welcome hugsql ----'''
    primary_keys=''
    for key,value in conf_dict.items():
        if 'fields_code-0' == key:
            primary_keys+='cast('+value+' as varchar),@'
        elif 'fields_code' in key:
            primary_keys+='\n\t,cast('+value+' as varchar),@'
        else:
            regex = r'({{[ ]*%s[ ]*}})'%(key)
            sql_content= re.sub(regex, value, sql_content)
    regex = r'({{[ ]*%s[ ]*}})'%('pk')
    sql_content= re.sub(regex, primary_keys, sql_content)

    return sql_content

def generator_dependencies_null_value_ratio_check(conf_dict:dict) -> str:
# 输入 conf_dict:{dep_dbtab:"";part_name:"";part_var:"";fields_code-0:'',fields_code-1:''}
# 输出 测试SQL生成-空值率
    sql_content='''---- welcome hugsql ----\n\n
select 
{{null_value_ratio_compute}}
from(
    select
        count(*) as rows
        {{null_value_cnt_compute}}
    from {{dep_dbtab}}
    where {{part_name}}='{{part_var}}'
)
    \n\n---- welcome hugsql ----'''
    null_value_cnt_compute=''
    null_value_ratio_compute=''
    for key,value in conf_dict.items():
        if 'fields_code-0' == key:
            null_cnt_compu_item=''',count(if({{field}} is not null and {{field}} <> '' and {{field}} <> '-9999',1,null)) as {{field}}_cnt'''
            regex = r'({{[ ]*%s[ ]*}})'%('field')
            null_value_cnt_compute += re.sub(regex, value, null_cnt_compu_item) 
            

            null_ratio_compu_item='''\t{{field}}_cnt * 1.000000/rows as {{field}}_ratio'''
            null_value_ratio_compute += re.sub(regex, value, null_ratio_compu_item)
        elif 'fields_code' in key:
            null_cnt_compu_item='''count(if({{field}} is not null and {{field}} <> '' and {{field}} <> '-9999',1,null)) as {{field}}_cnt'''
            regex = r'({{[ ]*%s[ ]*}})'%('field')
            null_cnt_compu_item = re.sub(regex, value, null_cnt_compu_item)## null_cnt_compu_item : 每个字段计算非空总量的SQL语句，需要分别去替换。
            null_value_cnt_compute +='\n\t,'+null_cnt_compu_item ## null_value_cnt_compute 所有字段对应计算非空量的SQL语句，需要进行汇总。

            null_ratio_compu_item='''{{field}}_cnt * 1.000000/rows as {{field}}_ratio'''
            null_ratio_compu_item = re.sub(regex, value, null_ratio_compu_item) ## null_ratio_compu_item 每个字段计算非空比率的SQL语句，需要分别去替换。
            null_value_ratio_compute+='\n\t,'+null_ratio_compu_item ## null_value_ratio_compute 所有字段对应计算非空比率的SQL语句，需要进行汇总。
        else:
            regex = r'({{[ ]*%s[ ]*}})'%(key)
            sql_content= re.sub(regex, value, sql_content)

    regex = r'({{[ ]*%s[ ]*}})'%('null_value_cnt_compute')
    sql_content= re.sub(regex, null_value_cnt_compute, sql_content)
    regex = r'({{[ ]*%s[ ]*}})'%('null_value_ratio_compute')
    sql_content= re.sub(regex, null_value_ratio_compute, sql_content)

    return sql_content

def generator_dependencies_monitor_of_enumerate_distribution(conf_dict:dict) -> str:
    sql_content='''---- welcome hugsql ----\n\n
select 
    {{fields_code-0}}
    ,count(*) as row_cnt
  from {{dep_dbtab}}
  where {{part_name}}='{{part_var}}'
  group by {{fields_code-0}} 
  limit 2000
    \n\n---- welcome hugsql ----'''
    for key,value in conf_dict.items():
        regex = r'({{[ ]*%s[ ]*}})'%(key)
        sql_content= re.sub(regex, value, sql_content)

    return sql_content

def generator_dependencies_json_format_check(conf_dict:dict) -> str:
    sql_content='''---- welcome hugsql ----\n\n
select 
    json_extract_scalar({{fields_code-0}},'$.{{json_structure}}') as json_value,{{fields_code-0}}
  from {{dep_dbtab}}
  where {{part_name}}='{{part_var}}'
  and (json_extract_scalar({{fields_code-0}},'$.{{json_structure}}') is not null
  or json_extract_scalar({{fields_code-0}},'$.{{json_structure}}') <> '')
  limit 2000
\n\n---- welcome hugsql ----'''
    for key,value in conf_dict.items():
        regex = r'({{[ ]*%s[ ]*}})'%(key)
        sql_content= re.sub(regex, value, sql_content)
    return sql_content
    
def generator_dependencies_time_format_check(conf_dict:dict) -> str:
    sql_content='''---- welcome hugsql ----\n\n
select 
    count(1)
  from {{dep_dbtab}}
  where {{part_name}}='{{part_var}}'
  and regexp_like({{fields_code-0}},'^{{time_reg}}$') <> true
\n\n---- welcome hugsql ----'''

    for key,value in conf_dict.items():
        regex = r'({{[ ]*%s[ ]*}})'%(key)
        sql_content= re.sub(regex, value, sql_content)
    return sql_content

def generator_dependencies_number_format_check(conf_dict:dict) -> str:
    sql_content='''---- welcome hugsql ----\n\n
select 
    count(1)
  from {{dep_dbtab}}
  where {{part_name}}='{{part_var}}'
  and regexp_like({{fields_code-0}},'^{{number_reg}}$') <> true
\n\n---- welcome hugsql ----'''

    for key,value in conf_dict.items():
        regex = r'({{[ ]*%s[ ]*}})'%(key)
        sql_content= re.sub(regex, value, sql_content)
    return sql_content

def generator_mutil_tab_join_miss_ratio(conf_dict:dict) -> str:
    sql_content='''---- welcome hugsql ----\n\n
select count(1) as cnt,'A>B' as type
from(select 
    {{fields}}
  from {{dep_dbtaba}}
  where {{part_namea}}='{{part_vara}}'
  except 
  select 
    {{fields}}
  from {{dep_dbtabb}}
  where {{part_nameb}}='{{part_varb}}'
)UNION ALL 
select count(1) as cnt,'A<B' as type
from(select 
    {{fields}}
  from {{dep_dbtabb}}
  where {{part_nameb}}='{{part_varb}}'
  except 
  select 
    {{fields}}
  from {{dep_dbtaba}}
  where {{part_namea}}='{{part_vara}}'
)
\n\n---- welcome hugsql ----'''
    fields=''
    for key,value in conf_dict.items():
        if 'fields_code-0' == key:
            fields+=value
        elif 'fields_code' in key:
            fields+='\n    ,'+value
        else:
            regex = r'({{[ ]*%s[ ]*}})'%(key)
            sql_content= re.sub(regex, value, sql_content)
    regex = r'({{[ ]*%s[ ]*}})'%('fields')
    sql_content= re.sub(regex, fields, sql_content)

    return sql_content

def generator_mutil_tab_join_rows(conf_dict:dict) -> str:
    sql_content='''---- welcome hugsql ----\n\n
select 
  count(1) as cnt,'A rows' as type
from {{dep_dbtaba}}
  where {{part_namea}}='{{part_vara}}'
union all 
select count(1) as cnt,'A could join B' as type
from(select 
    {{fields}}
  from {{dep_dbtabb}}
  where {{part_nameb}}='{{part_varb}}'
  
  insersect

  select 
    {{fields}}
  from {{dep_dbtaba}}
  where {{part_namea}}='{{part_vara}}'
\n\n---- welcome hugsql ----'''
    fields=''
    for key,value in conf_dict.items():
        if 'fields_code-0' == key:
            fields+=value
        elif 'fields_code' in key:
            fields+='\n    ,'+value
        else:
            regex = r'({{[ ]*%s[ ]*}})'%(key)
            sql_content= re.sub(regex, value, sql_content)
    regex = r'({{[ ]*%s[ ]*}})'%('fields')
    sql_content= re.sub(regex, fields, sql_content)

    return sql_content

def generator_idempotence_of_sorting(conf_dict:dict) -> str:
    sql_content='''---- welcome hugsql ----\n\n
select 
  *
from (
    select
    count(1) over(partition by {{fields}},{{rank_time_field}}) as cnt
    from {{dep_dbtab}}
    where {{part_name}}='{{part_var}}'
) t
where t.cnt > 1
\n\n---- welcome hugsql ----'''
    fields=''
    for key,value in conf_dict.items():
        if 'fields_code-0' == key:
            fields+=value
        elif 'fields_code' in key:
            fields+=','+value
        else:
            regex = r'({{[ ]*%s[ ]*}})'%(key)
            sql_content= re.sub(regex, value, sql_content)
    regex = r'({{[ ]*%s[ ]*}})'%('fields')
    sql_content= re.sub(regex, fields, sql_content)

    return sql_content

def generator_deliverables_data_row_count(conf_dict:dict) -> str:
# 输入 conf_dict:{dep_dbtab:"";part_name:"";part_var:""}
# 输出 测试SQL生成-交付表数据总量
    sql_content='''---- welcome hugsql ----\n\n
select 
  count(1) as rows_cnt
from {{dep_dbtab}}
where {{part_name}}='{{part_var}}' 

\n---- welcome hugsql ----
'''
    for key,value in conf_dict.items():
        regex = r'({{[ ]*%s[ ]*}})'%(key)
        sql_content= re.sub(regex, value, sql_content)

    return sql_content

# 一模一样
def generator_deliverables_primary_keys_test(conf_dict:dict) -> str:
# 输入 conf_dict:{dep_dbtab:"";part_name:"";part_var:"";fields_code-0:'',fields_code-1:''}
# 输出 测试SQL生成-交付物唯一组合键验证
    sql_content='''---- welcome hugsql ----\n\n
select 
    count(distinct 
    concat(
        {{pk}}
        ) as pk_cnt
    ,count(*) as row_cnt
  from {{dep_dbtab}}
  where {{part_name}}='{{part_var}}'
\n\n---- welcome hugsql ----'''
    primary_keys=''
    for key,value in conf_dict.items():
        if 'fields_code-0' == key:
            primary_keys+='cast('+value+' as varchar),@'
        elif 'fields_code' in key:
            primary_keys+='\n\t,cast('+value+' as varchar),@'
        else:
            regex = r'({{[ ]*%s[ ]*}})'%(key)
            sql_content= re.sub(regex, value, sql_content)
    regex = r'({{[ ]*%s[ ]*}})'%('pk')
    sql_content= re.sub(regex, primary_keys, sql_content)

    return sql_content

#一模一样
def generator_deliverables_null_value_ratio(conf_dict:dict) -> str:
# 输入 conf_dict:{dep_dbtab:"";part_name:"";part_var:"";fields_code-0:'',fields_code-1:''}
# 输出 测试SQL生成-空值率
    sql_content='''---- welcome hugsql ----\n\n
select 
{{null_value_ratio_compute}}
from(
    select
        count(*) as rows
        {{null_value_cnt_compute}}
    from {{dep_dbtab}}
    where {{part_name}}='{{part_var}}'
)
    \n\n---- welcome hugsql ----'''
    null_value_cnt_compute=''
    null_value_ratio_compute=''
    for key,value in conf_dict.items():
        if 'fields_code-0' == key:
            null_cnt_compu_item=''',count(if({{field}} is not null and {{field}} <> '' and {{field}} <> '-9999',1,null)) as {{field}}_cnt'''
            regex = r'({{[ ]*%s[ ]*}})'%('field')
            null_value_cnt_compute += re.sub(regex, value, null_cnt_compu_item) 
            

            null_ratio_compu_item='''\t{{field}}_cnt * 1.000000/rows as {{field}}_ratio'''
            null_value_ratio_compute += re.sub(regex, value, null_ratio_compu_item)
        elif 'fields_code' in key:
            null_cnt_compu_item='''count(if({{field}} is not null and {{field}} <> '' and {{field}} <> '-9999',1,null)) as {{field}}_cnt'''
            regex = r'({{[ ]*%s[ ]*}})'%('field')
            null_cnt_compu_item = re.sub(regex, value, null_cnt_compu_item)## null_cnt_compu_item : 每个字段计算非空总量的SQL语句，需要分别去替换。
            null_value_cnt_compute +='\n\t,'+null_cnt_compu_item ## null_value_cnt_compute 所有字段对应计算非空量的SQL语句，需要进行汇总。

            null_ratio_compu_item='''{{field}}_cnt * 1.000000/rows as {{field}}_ratio'''
            null_ratio_compu_item = re.sub(regex, value, null_ratio_compu_item) ## null_ratio_compu_item 每个字段计算非空比率的SQL语句，需要分别去替换。
            null_value_ratio_compute+='\n\t,'+null_ratio_compu_item ## null_value_ratio_compute 所有字段对应计算非空比率的SQL语句，需要进行汇总。
        else:
            regex = r'({{[ ]*%s[ ]*}})'%(key)
            sql_content= re.sub(regex, value, sql_content)

    regex = r'({{[ ]*%s[ ]*}})'%('null_value_cnt_compute')
    sql_content= re.sub(regex, null_value_cnt_compute, sql_content)
    regex = r'({{[ ]*%s[ ]*}})'%('null_value_ratio_compute')
    sql_content= re.sub(regex, null_value_ratio_compute, sql_content)

    return sql_content

#一模一样
def generator_deliverables_monitor_of_enumerate_distribution(conf_dict:dict) -> str:
    sql_content='''---- welcome hugsql ----\n\n
select 
    {{fields_code-0}}
    ,count(*) as row_cnt
  from {{dep_dbtab}}
  where {{part_name}}='{{part_var}}'
  group by {{fields_code-0}} 
  limit 2000
    \n\n---- welcome hugsql ----'''
    for key,value in conf_dict.items():
        regex = r'({{[ ]*%s[ ]*}})'%(key)
        sql_content= re.sub(regex, value, sql_content)

    return sql_content

#一模一样
def generator_deliverables_json_format_check(conf_dict:dict) -> str:
    sql_content='''---- welcome hugsql ----\n\n
select 
    json_extract_scalar({{fields_code-0}},'$.{{json_structure}}') as json_value,{{fields_code-0}}
  from {{dep_dbtab}}
  where {{part_name}}='{{part_var}}'
  and (json_extract_scalar({{fields_code-0}},'$.{{json_structure}}') is not null
  or json_extract_scalar({{fields_code-0}},'$.{{json_structure}}') <> '')
  limit 2000
\n\n---- welcome hugsql ----'''
    for key,value in conf_dict.items():
        regex = r'({{[ ]*%s[ ]*}})'%(key)
        sql_content= re.sub(regex, value, sql_content)
    return sql_content

#一模一样
def generator_deliverables_time_format_check(conf_dict:dict) -> str:
    sql_content='''---- welcome hugsql ----\n\n
select 
    count(1)
  from {{dep_dbtab}}
  where {{part_name}}='{{part_var}}'
  and regexp_like({{fields_code-0}},'^{{time_reg}}$') <> true
\n\n---- welcome hugsql ----'''

    for key,value in conf_dict.items():
        regex = r'({{[ ]*%s[ ]*}})'%(key)
        sql_content= re.sub(regex, value, sql_content)
    return sql_content

#一模一样
def generator_deliverables_number_format_check(conf_dict:dict) -> str:
    sql_content='''---- welcome hugsql ----\n\n
select 
    count(1)
  from {{dep_dbtab}}
  where {{part_name}}='{{part_var}}'
  and regexp_like({{fields_code-0}},'^{{number_reg}}$') <> true
\n\n---- welcome hugsql ----'''

    for key,value in conf_dict.items():
        regex = r'({{[ ]*%s[ ]*}})'%(key)
        sql_content= re.sub(regex, value, sql_content)
    return sql_content

def generator_white_namelist_check(conf_dict:dict) -> str:
    sql_content='''---- welcome hugsql ----\n\n
select
  *
from {{dep_dbtab}}
where {{part_name}}='{{part_var}}'
  and {{fields}}
\n\n---- welcome hugsql ----'''
    fields=''
    for key,value in conf_dict.items():
        if 'fields_code-0' == key:
            fields+=value
        elif 'fields_code' in key:
            fields+='\n  and '+value
        else:
            regex = r'({{[ ]*%s[ ]*}})'%(key)
            sql_content= re.sub(regex, value, sql_content)
    regex = r'({{[ ]*%s[ ]*}})'%('fields')
    sql_content= re.sub(regex, fields, sql_content)
    return sql_content

def generator_twin_dataset_rows_check(conf_dict:dict) -> str:
    sql_content='''---- welcome hugsql ----\n\n
select 
  count(1) -(
    select 
      count(1) 
    from {{dep_db}}_test.{{dep_tab}} 
    where {{part_name}}='{{part_var}}'
  ) as cnt_dif
from {{dep_db}}.{{dep_tab}} 
    where {{part_name}}='{{part_var}}'
\n\n---- welcome hugsql ----'''
    for key,value in conf_dict.items():
        regex = r'({{[ ]*%s[ ]*}})'%(key)
        sql_content= re.sub(regex, value, sql_content)

    return sql_content

def generator_data_dif_check(conf_dict:dict) -> str:
    sql_content='''---- welcome hugsql ----\n\n
select 
    *
from(select 
  {{pks}}
  ,{{fields}}
from {{dep_db}}.{{dep_tab}} 
    where {{part_name}}='{{part_var}}') pro
left join(select 
   {{pks}}
  ,{{fields}}
from {{dep_db}}_test.{{dep_tab}} 
where {{part_name}}='{{part_var}}'
) dev
on {{pk_join}}
where {{fields_filter}}
\n\n---- welcome hugsql ----'''
    pks=''
    fields=''
    pk_join=''
    fields_filter=''
    for key,value in conf_dict.items():
        if 'pk_fields_code-0' == key:
            pks+=value
            pk_join+='pro.'+value+'=dev.'+value
        elif 'pk_fields_code' in key:
            pks+='\n  ,'+value
            pk_join+='\n  and pro.'+value+'=dev.'+value
        elif 'field_fields_code-0' == key:
            fields+=value
            fields_filter+='pro.'+value+'<> dev.'+value
        elif 'field_fields_code' in key:
            fields+='\n  ,'+value
            fields_filter+='\n  and pro.'+value+'<> dev.'+value
        else:
            regex = r'({{[ ]*%s[ ]*}})'%(key)
            sql_content= re.sub(regex, value, sql_content)

    
    regex = r'({{[ ]*%s[ ]*}})'%('pks')
    sql_content= re.sub(regex, pks, sql_content)
    regex = r'({{[ ]*%s[ ]*}})'%('fields')
    sql_content= re.sub(regex, fields, sql_content)
    regex = r'({{[ ]*%s[ ]*}})'%('pk_join')
    sql_content= re.sub(regex, pk_join, sql_content)
    regex = r'({{[ ]*%s[ ]*}})'%('fields_filter')
    sql_content= re.sub(regex, fields_filter, sql_content)

    return sql_content