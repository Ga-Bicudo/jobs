import requests

curriculo = {              
	"full_name": "Gabriel Bicudo Rosa",
	"email": "gabrielbicudorosa@gmail.com",
	"mobile_phone": "+55 (11) 97646-1896",
	"age": 946283408,
	"home_address": "976, rua cantagalo, tatuapé, SP - São Paulo",
	"start_date": 1594731608,
	"opportunity_tag": "Python Developer",
	"past_jobs_experience": "i've worked as T.i. tecnitian, i used to go at our costumers company to do implementations, fixes and maintenances, then i was promoted to helpdesk of the company, solving issues remotly by teamviewer. Also, at my current job, im responsible for the support and as well, criation and changes of intern automations processes with python ",
	"degrees": [{
		"institution_name": "Unip-Tatuapé",
		"degree_name": "Ciencias da computação",
		"begin_date": 1550593448,
		"end_date": 1669393448
	}],
	"programming_skills": ["python", "java", "Javascript", 'c'],
	"database_skills": ["mysql"],
	"hobbies": ["Gym", "dating with some friends"],
	"why": "Not just by being a oportunidy of self improvement, i've done some reseachers about SciCrop, and i've got very impressed with such greatness. I believe that with my knowlodge and Skills, i can not just be productive at the current level of the company, but, do more to increase SciCrop in general ",
	"git_url_repositories": "https://github.com/Ga-Bicudo/jobs"
}

api = requests.post("https://engine.scicrop.com/scicrop-engine-web/api/v1/jobs/post_resume", json = curriculo) 

print(api)