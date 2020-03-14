# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 17:41:12 2018

@author: raghup
"""

query1 = "select left(due_dt,7)'date',,count(distinct case when state='CA' and original_apr<=36 then loanid end)'CA',count(distinct case when state='GA' and original_apr<=36 then loanid end)'GA',count(distinct case when state='ID' and original_apr<=36 then loanid end)'ID',count(distinct case when state='IL' and original_apr<=36 then loanid end)'IL',count(distinct case when state='MO' and original_apr<=36 then loanid end)'MO',count(distinct case when state='NM' and original_apr<=36 then loanid end)'NM',count(distinct case when state='SC' and original_apr<=36 then loanid end)'SC',count(distinct case when state='UT' and original_apr<=36 then loanid end)'UT' from ProductionDB.Equity_Deck_V2_20181107 inner join decision.contact using(lead_id) where PD_60<>-99 and 60_marginal_first = 1 group by 1 order by date;


states = [ 'GA'  ,  	 'MO',    	 'CA',    	 'IL',    	 'KS',    	 'AR',    	 'HI',    	 'VT',    	 'SC',    	 'FL',    	 'MT',    	 'TX',    	 'KY ',   	 'OH',    	 'MN',    	 'IN',    	 'PA',    	 'AZ',    	 'TN',    	'OK',    	 'MS',   	 'DE',    	 'NE',    	 'WA',    	 'RI',    	 'SD',    	 'NM',    	 'AL',    	 'UT',    	'AK',    	 'WI',   	 'MI',    	 'NC'    ]

q1 = ",count(distinct case when state='{state}' and original_apr<=36 then loanid end)'{state}'"
query = ''
for i in states:
    query+=q1.format(state=i)
    