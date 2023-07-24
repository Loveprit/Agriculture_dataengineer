create or replace table crop_dataengineer.analysis (
select ft.Area, ft.Yield, ft.Production, ft.Annual_Rainfall, ft.Fertilizer, ft.Pesticide,
cp.crop as crop, sn.season as season, st.state as state, yr.year as year   from `crop_dataengineer.fact_table` ft
join `crop_dataengineer.crop_dim` cp on ft.crop_id = cp.crop_id
join `crop_dataengineer.season_dim` sn on ft.season_id = sn.season_id
join `crop_dataengineer.state_dim` st on ft.state_id = st.state_id
join `crop_dataengineer.year_dim` yr on ft.year_id = yr.year_id)