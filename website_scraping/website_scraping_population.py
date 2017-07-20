import urllib2
import html2text
import pandas as pd
columns = ['population,population_density,area']
df = pd.DataFrame(columns=columns)

k = 100
while k < 1611:
	try:
		url='http://profile.id.com.au/brisbane/about?WebID='+str(k)
		page = urllib2.urlopen(url)
		html_content = page.read()
		rendered_content = html2text.html2text(html_content)
		f = open('file_text.txt', 'w')
		f.write(rendered_content)
		f.close()

		pop_line = 0
		pop_dens_line = 0
		area_line = 0
		
		
		get=open('file_text.txt','r')
		for i, line in enumerate(get):
			line=' '.join(line.split())
			if i == 114:
				suburb = line
				#print suburb
			
		
			if line == '### Population':
				pop_line = i+2
			
			if line == '### Population density':
				pop_dens_line = i+2
				#print line
		
			if line == '### Land area':
				area_line = i+2
				#print line
		
			if i == pop_line and i != 0:
				# print line
				population = line
		
			if i == pop_dens_line and i != 0:
				#print line
				population_density = line
		
			if i == area_line and i != 0:
				#print line
				area = line
		print suburb,':',population,':',population_density,':',area
		k = k +10
	except UnicodeDecodeError:
		k = k+10
		continue 
		

#df['population'] = population
#df['population_density'] = population_density
#df['area'] = area
#
#print df 