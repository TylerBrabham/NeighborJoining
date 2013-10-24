def neighborjoining(dis_map, n, L):
	if n==2:
		print dis_map
		return dis_map
	else:
		#calculate the r_i coefficients
		r = {}
		for (i,j) in dis_map:
			r[i] = 0

		for (i,j) in dis_map:
			r[i] += float(1/(float(n-2)))*float(dis_map[(i,j)])

		#calculate the Dij coefficients
		D = {}
		for (i,j) in dis_map:
				D[(i,j)] = dis_map[(i,j)]-r[i]-r[j]

		min_D = float('inf')
		min_i = -1
		min_j = -1
		for (i,j) in D:
			val = D[(i,j)]

			if val < min_D and i!=j:
				min_D = val
				min_i = i
				min_j = j

		print min_i, min_j

		#define new node n for minimal i and j
		new_dis_map = {}
		k = L
		for (i,j) in dis_map:
			#print min_i,min_j, i ,j
			if j==min_i or j==min_j:
				pass
			else:
				new_dis_map[(k,j)] = .5 * float(dis_map[(min_i,j)]+dis_map[(min_j,j)]-dis_map[(min_i,min_j)])
				new_dis_map[(j,k)] = new_dis_map[(k,j)]
		new_dis_map[(k,k)] = 0

		#remove min_i and min_j from dismap
		for (i,j) in dis_map:
			if i == min_i or j==min_j or i==min_j or j==min_i:
				pass
			else:
				#print i,j,min_i,min_j
				new_dis_map[(i,j)] = dis_map[(i,j)]

		#print new_dis_map
		d_ik = .5*float(dis_map[(min_i,min_j)] + r[min_i] - r[min_j])
		d_jk = dis_map[(min_i,min_j)] - d_ik

		print d_ik, d_jk

		#print new_dis_map
		neighborjoining(new_dis_map,n-1,L+1)



dis_data = open('data.txt')

dis_map = {}
i = 0
for line in dis_data:
	split_line = line.split()
	print split_line
	for j in range(len(split_line)):
		dis_map[(i,j)] = int(split_line[j])
	i+=1
dis_data.close()

neighborjoining(dis_map, 8,8)