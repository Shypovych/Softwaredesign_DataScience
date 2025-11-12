# c1 module
# UML Fact Checker

# Relation: University ⟶ Student (composition)
# Meaning: each Student belongs to exactly one University and cannot exist without it.

# c1.1 Can two universities have the same name?
#      No – 'name: string' is not marked as unique.

# c1.2 Can a university and a student share the same name?
#      No – UML does not restrict identical values across different classes.

# c1.3 Can a student study at more than one university?
#      No – composition allows only one parent (one university).

# c1.4 Does every student study at least at one university?
#      Yes – a student cannot exist without a university in composition.

# c1.5 Can two students with the same name study at the same university?
#      Yes – there is no uniqueness constraint on 'Student.name'.

# c1.6 Can two students with the same name study at different universities?
#      Yes – UML does not forbid it.

# c1.7 Can two universities have the same address?
#      Yes – 'address' is a regular attribute, not unique.

# UML uniqueness can be declared as:
#     name: String {unique}
