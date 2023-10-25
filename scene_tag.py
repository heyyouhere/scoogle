import os 
import json


class Project:
	def __init__(self, path, year, name, id):
		self.path = path
		self.year = year
		self.name = name
		self.id = id
		self.images = []
	def __str__(self):
		return(f"P:{self.path.encode('utf-8')}, N:{self.name.encode('utf-8')}, Y:{self.year.encode('utf-8')}")
	def toDic(self):
		return { "id": self.id,
			"checked": False,
			"name": self.name,
			"year": self.year,
			"images": self.images,
			"path": self.path,
			"event_tags": [],
			}
       



projects = []

folders = []
root_folders = []
result_dic = {}

first_time = True
counter = 0
for dirpath, b, c in os.walk('.'):
	if "эскизы" in dirpath or "Эскизы" in dirpath:
		files = []
		for file in c:
			if file.endswith(".jpg") or file.endswith(".pdf"):
				project_name = os.path.join(dirpath, file).split('\\')[2]
				project_year = os.path.join(dirpath, file).split('\\')[1]
				current_project = None
				for p in projects: 
					if p.name == project_name and p.year == project_year:
						current_project = p
						break
				if not current_project:		
					print("Creating new project")
					current_project = Project(dirpath, project_year, project_name, counter)
					projects.append(current_project)
					counter += 1
				current_project.images.append(os.path.join(dirpath,file))

print(len(projects))
for p in projects:
	f = open(p.name + ".json", 'w', encoding='utf-8') 
	json.dump(p.toDic(), f)
	f.close()
print("All done")
