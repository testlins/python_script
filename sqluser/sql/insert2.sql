 use kangvahealth
 if not exists(select 1 from ph_family where familyno='630121100010000002')
 begin
 INSERT  INTO ph_family
 ([dutydoc]       ,[hosid]     ,[name]       ,[pycode]       ,[wbcode] ,[address]      ,[tel] ,familyno ) 
 VALUES('测试人员', '0001001', '测试' , 'CS','IY', '大通回族土族自治县桥头镇人民路南居委会', '', '630121100010000002')
 end