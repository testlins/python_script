 use kangvahealth
 if not exists(select 1 from ph_family where familyno='630121100010000002')
 begin
 INSERT  INTO ph_family
 ([dutydoc]       ,[hosid]     ,[name]       ,[pycode]       ,[wbcode] ,[address]      ,[tel] ,familyno ) 
 VALUES('������Ա', '0001001', '����' , 'CS','IY', '��ͨ����������������ͷ������·�Ͼ�ί��', '', '630121100010000002')
 end