# Register the submod
init -990 python:
    store.mas_submod_utils.Submod(
        author="TheGamerSide67",
        name="Mental Disabilities Submod",
        description="A large submod dedicated to the talk of philosophy and mental disabilites and more!",
        version="1.4",
    )

# Register the updater
init -989 python:
    
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="Mental Disabilities Submod",
            user_name="TheGamerSide67",
            repository_name="MentalDisabilitySubmod",
            extraction_depth=2
        )

