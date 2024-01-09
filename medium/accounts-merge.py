class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # get the aacounts one by one and add to a new list called solution, and for each email add it to a disctionary like d[email] = id, where id is the position in the solution list where the email is. Before adding a new account to solution, we check in d if the email has already appeared. If is did, we do not append this account in the solution, but we add these emails to the solution[id]. 


        d = {}  # hold the key email, and item is the id in the solution list that the email is 

        solution = []

        for account in accounts:
            name = account[0]
            emails = account[1:]

           
            account_appeared = False
            ids = set()
            for email in emails: # check if the email has already appeared
                if email in d:
                    account_appeared = True
                    ids.add(d[email]) 
            if account_appeared:
                # we add the new emails to the previously inserted account in solutions, in id_
                ids_list = list(ids)
                id_ = ids_list[0]
                for email in emails:
                    if not email in d:
                        solution[id_].append(email)
                        d[email] = id_
                
                # now merge all accounts from ids, because they correspond to the same person. We will merge them to the id[0]
                if len(ids) > 1:
                    for id_ in ids_list[1:]:
                        merged_account = []
                        merged_emails = solution[ids_list[0]][1:] + solution[id_][1:]
                        
                        # get only the unique emais, not repeated
                        merged_emails_set = set()
                        for e in merged_emails:
                            merged_emails_set.add(e)
                        merged_emails = list(merged_emails_set)

                        solution[ids_list[0]] = [solution[ids_list[0]][0]] + sorted(merged_emails) # merged the solution in the first id
                        solution[id_] = None # remove content in the onther id

                        # #update the ids in the disctionary d
                        for email in solution[ids_list[0]][1:]:
                            d[email] = ids_list[0]
        
            
            else:
                # append the new account to solution
                solution.append([name])

                id_ = len(solution) - 1
                # mark the emails as seen and save their ids
                for email in emails:
                    if not email in d:
                        solution[-1].append(email)
                        d[email] = id_
        
        clean_solution = []
        for id_ in range(0,len(solution)):
            if solution[id_]: # removing the NONE accounts
                clean_solution.append( [solution[id_][0]] + sorted(solution[id_][1:]) ) # the emails must be in sorted order
            
        return clean_solution