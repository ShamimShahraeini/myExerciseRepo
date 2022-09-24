def sort_dependencies(packages, package_name):
    package_dependencies = []
    if package_name in packages:
        sub_packages = packages[package_name]
        package_dependencies = sub_packages + package_dependencies
        
        if sub_packages == []:
            package_dependencies = list(dict.fromkeys(package_dependencies))
            return package_dependencies

        for package in sub_packages:
            new_sub_packages = sort_dependencies(packages, package)
            package_dependencies = new_sub_packages + package_dependencies

    package_dependencies = list(dict.fromkeys(package_dependencies))
    return package_dependencies


# packages = {'pkg1': ['pkg3'], 'pkg2':['pkg3'], 'pkg3': [], 'pkg4':['pkg1', 'pkg2']}
# package_name = 'pkg4'

# package_dependencies = sort_dependencies(packages, package_name)
# print(package_dependencies)