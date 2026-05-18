# Component View Diagram

```mermaid
flowchart TD

    CreateUser[CreateUserUseCase]
    ResolvePermissions[ResolvePermissionsUseCase]
    AssembleContext[AssembleIdentityContextUseCase]

    UserEntity[User]
    RoleEntity[Role]
    PermissionEntity[Permission]

    UserRepository[UserRepository]
    RoleRepository[RoleRepository]

    SQLAlchemyUserRepo[SQLAlchemyUserRepository]
    SQLAlchemyRoleRepo[SQLAlchemyRoleRepository]

    PostgreSQL[(PostgreSQL)]

    CreateUser --> UserEntity
    ResolvePermissions --> RoleEntity
    ResolvePermissions --> PermissionEntity

    AssembleContext --> UserRepository
    AssembleContext --> RoleRepository

    UserRepository --> SQLAlchemyUserRepo
    RoleRepository --> SQLAlchemyRoleRepo

    SQLAlchemyUserRepo --> PostgreSQL
    SQLAlchemyRoleRepo --> PostgreSQL
