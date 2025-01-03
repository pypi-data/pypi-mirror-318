from virtuals_sdk import game

VIRTUALS_API_KEY = "cd3dad11eaa9d97037b1d4e9ead9bed47b3eaef187f06c18bb9288edc6d2b076"
# Create agent with just strings for each component
agent = game.Agent(
    api_key=VIRTUALS_API_KEY,
    goal="You are trying to apply for a job in finance that pays a lot of money. Research to get more information on the biggest banks in the world.",
    description="",
    world_info=""
)

agent.list_available_default_twitter_functions().keys()
agent.use_default_twitter_functions(['like_tweet'])

x = game.Function(
        fn_name="get_company_info",
        fn_description="Get information on a company, given the company name",
        args=[
            game.FunctionArgument(
                name="company_url",
                type="string",
                description="Provide the website of the biggest bank in the world. Remove the prefix related to http, https or www."
            )
        ],
        config=game.FunctionConfig(
            method="get",
            url="https://sekoia-apis.vercel.app/api/get_company_info?company_url={{company_url}}",
            platform="twitter",
            success_feedback="Company info search for {{company_url}} was successful. {{response.company_info.name}} (legally known as {{response.company_info.legal_name}}) is a company offering a wide range of financial solutions.",
            error_feedback="There was an error. Please try again later.",
        )
    )

company_url = 'www.jpmorgan.com'
x(company_url)

agent.add_custom_function(x)

response = agent.simulate_twitter(session_id="testy-1")
print(response)