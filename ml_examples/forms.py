from django import forms

JOB_TITLES = {
    ('Medical Receptionist' , 'Medical Receptionist'),
    ('Clinical Research Associate' , 'Clinical Research Associate'),
    ('Territory Sales Representative' , 'Territory Sales Representative'),
    ('Bus Driver' , 'Bus Driver'),
    ('Foreign Service Officer' , 'Foreign Service Officer'),
    ('Sales Analyst' , 'Sales Analyst'),
    ('Strategy Consultant?' , 'Strategy Consultant?'),
    ('Cost Engineer' , 'Cost Engineer'),
    ('Solutions Consultant - Electrical Engineering' , 'Solutions Consultant - Electrical Engineering'),
    ('Power Regulator' , 'Power Regulator'),
    ('Conservation Technician' , 'Conservation Technician'),
    ('Manager of Engineering' , 'Manager of Engineering'),
    ('Forecast Systems Manager' , 'Forecast Systems Manager'),
    ('Water Services Technician' , 'Water Services Technician'),
    ('Senior Analyst Retail Analytics and Reporting' , 'Senior Analyst Retail Analytics and Reporting'),
    ('Total Quality Management Director' , 'Total Quality Management Director'),
    ('HVAC Mechanic' , 'HVAC Mechanic'),
    ('Cognos Business Development Architect' , 'Cognos Business Development Architect'),
    ('School Social Worker' , 'School Social Worker'),
    ('Treasurer' , 'Treasurer'),
    ('Manufacturing Customer Service Representative' , 'Manufacturing Customer Service Representative'),
    ('Quality Assurance Manager' , 'Quality Assurance Manager'),
    ('Night Auditor' , 'Night Auditor'),
    ('Medical Receptionist' , 'Medical Receptionist'),
    ('Business Intelligence Developer' , 'Business Intelligence Developer'),
    ('Solid Waste Field Technician' , 'Solid Waste Field Technician'),
    ('Healthcare Consultant' , 'Healthcare Consultant'),
    ('Organic Lab Worker' , 'Organic Lab Worker'),
    ('Compliance Engineer' , 'Compliance Engineer'),
    ('Chief of Career Pathways and Integrated Learning' , 'Chief of Career Pathways and Integrated Learning'),
    ('Assistant Coach' , 'Assistant Coach'),
    ('IT Support Staff' , 'IT Support Staff'),
    ('Meeting Specialist' , 'Meeting Specialist'),
    ('Freelance Travel Writer' , 'Freelance Travel Writer'),
    ('Account Executive' , 'Account Executive'),
    ('Process Engineer' , 'Process Engineer'),
    ('Catering Manager' , 'Catering Manager'),
    ('Roadie' , 'Roadie'),
    ('Research and Development Technician' , 'Research and Development Technician'),
    ('Human Resources Assistant' , 'Human Resources Assistant'),
    ('Solar Installers' , 'Solar Installers'),
    ('Travel Consultant' , 'Travel Consultant'),
    ('Stationary Engineer' , 'Stationary Engineer'),
    ('Material Handler' , 'Material Handler'),
    ('Healthcare Business Intelligence Manager' , 'Healthcare Business Intelligence Manager'),
    ('Quality Assurance Technologist' , 'Quality Assurance Technologist'),
    ('Staff Assistant - Accounting' , 'Staff Assistant - Accounting'),
    ('Staff Engineer' , 'Staff Engineer'),
    ('Assistant Technician' , 'Assistant Technician'),
    ('Strategy Consultant?' , 'Strategy Consultant?'),
    ('Project Manager' , 'Project Manager'),
    ('Engineering Technician' , 'Engineering Technician'),
    ('Solution Architect Business Intelligence' , 'Solution Architect Business Intelligence'),
    ('Market Access Associate' , 'Market Access Associate'),
    ('Operations Research Analysis Manager' , 'Operations Research Analysis Manager'),
    ('Bellman' , 'Bellman'),
    ('Real Estate Appraiser' , 'Real Estate Appraiser'),
    ('Human Resources Director' , 'Human Resources Director'),
    ('Crew Scheduling Manager' , 'Crew Scheduling Manager'),
    ('Total Quality Management Director' , 'Total Quality Management Director'),
    ('Controller' , 'Controller'),
    ('Senior Manager Yield and Revenue Management' , 'Senior Manager Yield and Revenue Management'),
    ('Transportation Project Manager' , 'Transportation Project Manager'),
    ('Chemical Technician' , 'Chemical Technician'),
    ('Investment Advisor' , 'Investment Advisor'),
    ('Oceanographer' , 'Oceanographer'),
    ('Sales Coordinator' , 'Sales Coordinator'),
    ('Concierge' , 'Concierge'),
    ('Institutional Research Business Intelligence Systems Analyst' , 'Institutional Research Business Intelligence Systems Analyst'),
    ('Producer' , 'Producer'),
    ('Commercial Sales Representative' , 'Commercial Sales Representative'),
    ('Electrical Design Engineer' , 'Electrical Design Engineer'),
    ('Marketing Consultant' , 'Marketing Consultant'),
    ('Senior Manager of Industry Analytics' , 'Senior Manager of Industry Analytics'),
    ('Valet Parker' , 'Valet Parker'),
    ('Organic Lab Research Assistant' , 'Organic Lab Research Assistant'),
    ('Pharmacy Assistant' , 'Pharmacy Assistant'),
    ('Meeting Specialist' , 'Meeting Specialist'),
    ('Lineman' , 'Lineman'),
    ('Golf Pro' , 'Golf Pro'),
    ('Principal Service Engineer' , 'Principal Service Engineer'),
    ('Retail Sales Associate' , 'Retail Sales Associate'),
    ('Group Sales Management' , 'Group Sales Management'),
    ('Club Representative' , 'Club Representative'),
    ('Client Service Specialist' , 'Client Service Specialist'),
    ('Operations Clerk' , 'Operations Clerk'),
    ('Technical Support Engineer' , 'Technical Support Engineer'),
    ('Special Education Teacher' , 'Special Education Teacher'),
    ('Travel Secretary' , 'Travel Secretary'),
    ('Reservoir Engineer' , 'Reservoir Engineer'),
    ('Quality Assistant' , 'Quality Assistant'),
    ('Project Manager' , 'Project Manager'),
    ('Business Intelligence Developer' , 'Business Intelligence Developer'),
    ('Government Contract Consultant' , 'Government Contract Consultant'),
    ('General Manager' , 'General Manager'),
    ('Software Developer' , 'Software Developer'),
    ('Research and Development Tester' , 'Research and Development Tester'),
    ('Corporate Sales Manager' , 'Corporate Sales Manager'),
    ('Director of? Customer Success and Satisfaction' , 'Director of? Customer Success and Satisfaction'),
    ('Catering Account Manger' , 'Catering Account Manger'),
    ('Assistant Customer Care Center Manager' , 'Assistant Customer Care Center Manager'),
    ('Manufacturing Specialist' , 'Manufacturing Specialist'),
    ('Piping Stress Engineer' , 'Piping Stress Engineer'),
    ('RF Engineer' , 'RF Engineer'),
    ('Rental Representative' , 'Rental Representative'),
    ('Data Architect' , 'Data Architect'),
    ('Organizational Development Consultant' , 'Organizational Development Consultant'),
    ('Drilling Engineer' , 'Drilling Engineer'),
    ('Station Agent' , 'Station Agent'),
    ('Hostess' , 'Hostess'),
    ('School Nurse' , 'School Nurse'),
    ('Behavior Specialist' , 'Behavior Specialist'),
    ('Construction Engineer' , 'Construction Engineer'),
    ('Corporate Reservations Agent' , 'Corporate Reservations Agent'),
    ('Chef' , 'Chef'),
    ('Account Executive' , 'Account Executive'),
    ('Athletic Scout' , 'Athletic Scout'),
    ('Threat Intelligence Analyst' , 'Threat Intelligence Analyst'),
    ('Environmental Compliance Engineer' , 'Environmental Compliance Engineer'),
    ('Senior Mechanical Engineer' , 'Senior Mechanical Engineer'),
    ('Customer Support Associate' , 'Customer Support Associate'),
    ('Associate Producer Events' , 'Associate Producer Events'),
    ('Sales Manager' , 'Sales Manager'),
    ('Pharmacy Assistant' , 'Pharmacy Assistant'),
    ('Corporate Recruiter' , 'Corporate Recruiter'),
    ('Ground Support Equipment Mechanic' , 'Ground Support Equipment Mechanic'),
    ('Software Engineer - Data Warehouse/Business Intelligence' , 'Software Engineer - Data Warehouse/Business Intelligence'),
    ('Network Engineer' , 'Network Engineer'),
    ('Global Development Specialist' , 'Global Development Specialist'),
    ('Fabricator' , 'Fabricator'),
    ('Technology Consultant' , 'Technology Consultant'),
    ('Patient Care Coordinator' , 'Patient Care Coordinator'),
    ('Senior Manager Product Intelligence and Cost Analytics' , 'Senior Manager Product Intelligence and Cost Analytics'),
    ('Countertop Fabricator and Installer' , 'Countertop Fabricator and Installer'),
    ('Cruise Ship' , 'Cruise Ship'),
    ('Institutional Research Business Intelligence Systems Analyst' , 'Institutional Research Business Intelligence Systems Analyst'),
    ('Director of Hotel Sales' , 'Director of Hotel Sales'),
    ('Treasurer' , 'Treasurer'),
    ('Commercial Print Management Consultant' , 'Commercial Print Management Consultant'),
    ('Instrumentation Engineer' , 'Instrumentation Engineer'),
    ('Competitive Intelligence Manager' , 'Competitive Intelligence Manager'),
    ('Firmware Engineer' , 'Firmware Engineer'),
    ('Dermatology Nurse' , 'Dermatology Nurse'),
    ('Production Assistant Events' , 'Production Assistant Events'),
    ('Alarm Technician' , 'Alarm Technician'),
    ('Sports Physician' , 'Sports Physician'),
    ('Guest Room Sales Manager' , 'Guest Room Sales Manager'),
    ('Hunting Guide' , 'Hunting Guide'),
    ('Server' , 'Server'),
    ('Guest Services Agent' , 'Guest Services Agent'),
    ('Wedding Sales Manager' , 'Wedding Sales Manager'),
    ('Concierge?' , 'Concierge?'),
    ('Industrial Technology Teacher' , 'Industrial Technology Teacher'),
    ('Front Desk Clerk' , 'Front Desk Clerk'),
    ('Tax Advisor' , 'Tax Advisor'),
    ('Executive Conference Manager' , 'Executive Conference Manager'),
    ('Engineering Technician' , 'Engineering Technician'),
    ('Vice President of Engineering' , 'Vice President of Engineering'),
    ('Change Management Consultant' , 'Change Management Consultant'),
    ('Financial Analyst' , 'Financial Analyst'),
    ('Online Customer Support' , 'Online Customer Support'),
    ('Cook' , 'Cook'),
    ('Club Representative' , 'Club Representative'),
    ('Associate Athletic Director' , 'Associate Athletic Director'),
    ('Front Desk Manager' , 'Front Desk Manager'),
    ('Tile Setter' , 'Tile Setter'),
    ('Technology Research Manager' , 'Technology Research Manager'),
    ('Rotating Equipment Engineer' , 'Rotating Equipment Engineer'),
    ('Director of Hotel Operations' , 'Director of Hotel Operations'),
    ('Night Auditor' , 'Night Auditor'),
    ('Bus Driver' , 'Bus Driver'),
    ('Front End Load Driver' , 'Front End Load Driver'),
    ('Oracle Technical Lead' , 'Oracle Technical Lead'),
    ('Informatica Extract Transform Load (ETL) Developer' , 'Informatica Extract Transform Load (ETL) Developer'),
    ('Financial Analyst' , 'Financial Analyst'),
    ('Mining Safety Engineer' , 'Mining Safety Engineer'),
    ('Front Desk Associate' , 'Front Desk Associate'),
    ('Forecast Systems Manager' , 'Forecast Systems Manager'),
    ('Director of Guidance' , 'Director of Guidance'),
    ('Service Consultant' , 'Service Consultant'),
    ('Account Manager' , 'Account Manager'),
    ('Business Objects Architect' , 'Business Objects Architect'),
    ('Assistant Principal' , 'Assistant Principal'),
    ('Integration/Business Intelligence Technical Lead' , 'Integration/Business Intelligence Technical Lead'),
    ('Online Customer Support' , 'Online Customer Support'),
    ('Choral Music Teacher' , 'Choral Music Teacher'),
    ('Quality Control Engineer' , 'Quality Control Engineer'),
    ('Conference Coordinator' , 'Conference Coordinator'),
    ('Freelance Travel Writer' , 'Freelance Travel Writer'),
    ('Transportation Project Manager' , 'Transportation Project Manager'),
    ('Strength and Conditioning Coach' , 'Strength and Conditioning Coach'),
    ('Field Technician' , 'Field Technician'),
    ('Manager Special Events' , 'Manager Special Events'),
    ('Benefit Coordinator' , 'Benefit Coordinator'),
    ('Referee' , 'Referee'),
    ('Bus Driver' , 'Bus Driver'),
    ('Controls Engineer' , 'Controls Engineer'),
    ('Implementation Consultant' , 'Implementation Consultant'),
    ('Competitive Intelligence Manager' , 'Competitive Intelligence Manager'),
    ('Health/Physical Education Teacher' , 'Health/Physical Education Teacher'),
    ('Mechanical Engineer' , 'Mechanical Engineer'),
    ('Customer Service Agent' , 'Customer Service Agent'),
    ('Endoscopy Nurse' , 'Endoscopy Nurse'),
    ('Metal Building Erector' , 'Metal Building Erector'),
    ('Aviation Inside Sales' , 'Aviation Inside Sales'),
    ('Maintenance Engineer' , 'Maintenance Engineer'),
    ('Front Desk Associate' , 'Front Desk Associate'),
    ('Technical Writer' , 'Technical Writer'),
    ('Research and Development Tester' , 'Research and Development Tester'),
    ('Ethics Office Business Intelligence Officer' , 'Ethics Office Business Intelligence Officer'),
    ('Technical Trainer' , 'Technical Trainer'),
    ('Pipeline Engineer' , 'Pipeline Engineer'),
    ('Computer Science Teacher' , 'Computer Science Teacher'),
    ('Market Access Associate' , 'Market Access Associate'),
    ('Concrete Finisher' , 'Concrete Finisher'),
    ('Patio Room Installer' , 'Patio Room Installer'),
    ('Provisioning Agents' , 'Provisioning Agents'),
    ('Passenger Service Agent' , 'Passenger Service Agent'),
    ('International Education Coordinator' , 'International Education Coordinator'),
    ('Pipefitter' , 'Pipefitter'),
    ('Laboratory Sales Consultant' , 'Laboratory Sales Consultant'),
    ('Territory Service Representative' , 'Territory Service Representative'),
    ('Process Control Engineer' , 'Process Control Engineer'),
    ('Laboratory Assistant' , 'Laboratory Assistant'),
    ('Component Engineer' , 'Component Engineer'),
    ('Vice Principal' , 'Vice Principal'),
    ('Producer Travel Channel' , 'Producer Travel Channel'),
    ('Attorney' , 'Attorney'),
    ('Quality Associate/Validation' , 'Quality Associate/Validation'),
    ('Executive Conference Manager' , 'Executive Conference Manager'),
    ('Station Agent' , 'Station Agent'),
    ('Cardiovascular Operating Room Nurse' , 'Cardiovascular Operating Room Nurse'),
    ('Cyber Intelligence Watch Officer' , 'Cyber Intelligence Watch Officer'),
    ('Compensation Manager' , 'Compensation Manager'),
    ('Heavy Equipment Technician' , 'Heavy Equipment Technician'),
    ('Electronics Engineer' , 'Electronics Engineer'),
    ('Benefit Coordinator' , 'Benefit Coordinator'),
    ('Chemical Engineer' , 'Chemical Engineer'),
    ('Front Desk Attendant' , 'Front Desk Attendant'),
    ('Sales and Marketing Coordinator' , 'Sales and Marketing Coordinator'),
    ('Environmental Project Analyst' , 'Environmental Project Analyst'),
    ('International Travel Consultant' , 'International Travel Consultant'),
    ('Airline Pilot' , 'Airline Pilot'),
    ('Catering Account Manger' , 'Catering Account Manger'),
    ('Senior Competitive Intelligence Manager' , 'Senior Competitive Intelligence Manager'),
    ('Threat Intelligence Analyst' , 'Threat Intelligence Analyst'),
    ('Environmental Services Representative' , 'Environmental Services Representative'),
    ('Assistant General Manager' , 'Assistant General Manager'),
    ('Operations Agent' , 'Operations Agent'),
    ('Event Coordinator' , 'Event Coordinator'),
    ('Mutual Fund Analyst' , 'Mutual Fund Analyst'),
    ('Director of Hotel Sales' , 'Director of Hotel Sales')

}

class dreamJobForm(forms.Form):
    job_title = forms.CharField(label='Dream Job:', widget=forms.Select(choices=JOB_TITLES))
    