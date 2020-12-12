# sql server dbcc 工具使用
## dbcc 可使用命令连接
[dbcc 命名使用连接](https://docs.microsoft.com/en-us/sql/t-sql/database-console-commands/dbcc-transact-sql?view=sql-server-ver15)
## 查询索引情况
``` sql
-- 查看碎片化情况
dbcc showcontig(t_hr_ats_scheduleshiftItem);
-- 重建索引
DBCC DBREINDEX(t_hr_ats_scheduleshiftItem);
-- 查看索引
EXEC Sp_helpindex t_hr_ats_scheduleshiftItem;
```
### 排班查询慢可以尝试重建这几个表
```cmd
t_hr_ats_scheduleshift
t_hr_ats_scheduleshiftItem
T_HR_ATS_AttendanceFileHis
T_HR_ATS_AttendanceFile
T_ORG_Admin
t_bd_person
t_hr_ats_shift
t_org_admin
t_org_hro
```
```sql
dbcc showcontig(t_hr_ats_scheduleshift);
dbcc showcontig(t_hr_ats_scheduleshiftItem);
dbcc showcontig(T_HR_ATS_AttendanceFileHis);
dbcc showcontig(T_HR_ATS_AttendanceFile);
dbcc showcontig(t_bd_person);
dbcc showcontig(t_hr_ats_shift);
dbcc showcontig(t_org_admin);
dbcc showcontig(t_org_hro);

dbcc dbReindex(t_hr_ats_scheduleshift);
dbcc dbReindex(t_hr_ats_scheduleshiftItem);
dbcc dbReindex(T_HR_ATS_AttendanceFileHis);
dbcc dbReindex(T_HR_ATS_AttendanceFile);
dbcc dbReindex(t_bd_person);
dbcc dbReindex(t_hr_ats_shift);
dbcc dbReindex(t_org_admin);
dbcc showcontig(t_org_hro);

select * from t_hr_ats_scheduleshift;
select * from t_hr_ats_scheduleshiftItem;
select * from T_HR_ATS_AttendanceFileHis;
select * from T_HR_ATS_AttendanceFile;
select * from T_ORG_Admin;
select * from t_bd_person;
select * from t_hr_ats_shift;
select * from t_org_admin;
select * from t_org_hro;

```
### 输出分析
```sql 
dbcc showcontig(t_hr_ats_scheduleshiftItem);
/*
重建索引之前：
DBCC SHOWCONTIG scanning 'T_HR_ATS_ScheduleShiftItem' table...
Table: 'T_HR_ATS_ScheduleShiftItem' (159196213); index ID: 1, database ID: 10
TABLE level scan performed.
- Pages Scanned................................: 5974
- Extents Scanned..............................: 752
- Extent Switches..............................: 5841
- Avg. Pages per Extent........................: 7.9
- Scan Density [Best Count:Actual Count].......: 12.79% [747:5842]
- Logical Scan Fragmentation ..................: 96.64%
- Extent Scan Fragmentation ...................: 51.60%
- Avg. Bytes Free per Page.....................: 3728.5
- Avg. Page Density (full).....................: 53.93%
DBCC execution completed. If DBCC printed error messages, contact your system administrator.

*/

DBCC DBREINDEX(t_hr_ats_scheduleshiftItem);

dbcc showcontig(t_hr_ats_scheduleshiftItem);
/*
重建索引之后：
DBCC SHOWCONTIG scanning 'T_HR_ATS_ScheduleShiftItem' table...
Table: 'T_HR_ATS_ScheduleShiftItem' (159196213); index ID: 1, database ID: 10
TABLE level scan performed.
- Pages Scanned................................: 3255
- Extents Scanned..............................: 407
- Extent Switches..............................: 406
- Avg. Pages per Extent........................: 8.0
- Scan Density [Best Count:Actual Count].......: 100.00% [407:407]
- Logical Scan Fragmentation ..................: 0.00%
- Extent Scan Fragmentation ...................: 9.58%
- Avg. Bytes Free per Page.....................: 122.8
- Avg. Page Density (full).....................: 98.48%
DBCC execution completed. If DBCC printed error messages, contact your system administrator.
*/

```
### dbcc showcontig 信息说明
* Page Scanned-扫描页数：如果你知道行的近似尺寸和表或索引里的行数，那么你可以估计出索引里的页数。看看扫描页数，如果明显比你估计的页数要高，说明存在内部碎片。 
* Extents Scanned-扫描扩展盘区数：用扫描页数除以8,四舍五入到下一个最高值。该值应该和DBCC SHOWCONTIG返回的扫描扩展盘区数一致。如果DBCC SHOWCONTIG返回的数高，说明存在外部碎片。碎片的严重程度依赖于刚才显示的值比估计值高多少。 
* Extent Switches-扩展盘区开关数：该数应该等于扫描扩展盘区数减1。高了则说明有外部碎片。 
* Avg. Pages per Extent-每个扩展盘区上的平均页数：该数是扫描页数除以扫描扩展盘区数，一般是8。小于8说明有外部碎片。 
* Scan Density [Best Count:Actual Count]-扫描密度［最佳值:实际值］：DBCC SHOWCONTIG返回最有用的一个百分比。这是扩展盘区的最佳值和实际值的比率。该百分比应该尽可能靠近100％。低了则说明有外部碎片。
* Logical Scan Fragmentation-逻辑扫描碎片：无序页的百分比。该百分比应该在0％到10％之间，高了则说明有外部碎片。 
* Extent Scan Fragmentation-扩展盘区扫描碎片：无序扩展盘区在扫描索引叶级页中所占的百分比。该百分比应该是0％，高了则说明有外部碎片。 
* Avg. Bytes Free per Page-每页上的平均可用字节数：所扫描的页上的平均可用字节数。越高说明有内部碎片，不过在你用这个数字决定是否有内部碎片之前，应该考虑fill factor（填充因子）。 
* Avg. Page Density (full)-平均页密度（完整）：每页上的平均可用字节数的百分比的相反数。低的百分比说明有内部碎片
