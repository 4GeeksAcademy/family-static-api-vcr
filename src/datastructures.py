"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 4  # Já temos 3 IDs usados, próximo ID será 4
        self._members = [
            {"id": 1, "first_name": "John", "age": 33, "lucky_numbers": [7, 13, 22]},
            {"id": 2, "first_name": "Jane", "age": 35, "lucky_numbers": [10, 14, 3]},
            {"id": 3, "first_name": "Jimmy", "age": 5, "lucky_numbers": [1]}
        ]

    def _generate_id(self):
        """Gera um ID único"""
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        """Adiciona um membro à lista de membros"""
        member["id"] = member.get("id", self._generate_id())
        member["last_name"] = self.last_name
        member["lucky_numbers"] = list(member.get("lucky_numbers", []))
        self._members.append(member)
        return member

    def delete_member(self, id):
        """Remove o membro com base no ID"""
        initial_length = len(self._members)
        self._members = [m for m in self._members if m["id"] != id]
        return len(self._members) < initial_length

    def get_member(self, id):
        """Retorna o membro que tem o ID especificado"""
        for member in self._members:
            if member["id"] == int(id):
                return member  # Retorna o membro completo
        return None

    def get_all_members(self):
        """Retorna todos os membros da família"""
        return self._members
