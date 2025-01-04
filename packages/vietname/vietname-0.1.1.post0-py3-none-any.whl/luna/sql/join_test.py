from .blocks import SqlTarget
from .join import JoinBlock, JoinTarget


def test_joins(ctx):
    person = SqlTarget(
        name="person",
        target="person",
        fields=[{"name": "id"}, {"name": "name"}, {"name": "age"}, {"name": "department_id"}, {"name": "school_id"}],
    )
    department = SqlTarget(
        name="department", target="department", fields=[{"name": "id"}, {"name": "name"}, {"name": "company_id"}]
    )
    company = SqlTarget(name="company", target="company", fields=[{"name": "id"}, {"name": "name"}])
    school = SqlTarget(name="school", target="school", fields=[{"name": "id"}, {"name": "name"}])

    join = JoinBlock(
        base=person,
        joins=[
            JoinTarget(target=department, condition="person.department_id = department.id", alias="department"),
            JoinTarget(target=company, condition="department.company_id = company.id", alias="company"),
            JoinTarget(target=school, condition="person.school_id = school.id", alias="school"),
        ],
    )

    sql = join.to_sql()

    print(sql)
