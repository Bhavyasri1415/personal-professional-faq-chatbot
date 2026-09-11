faq_patterns = {

    # ---------------- GREETINGS ----------------

    r"(hi|hello|hey|good morning|good afternoon|good evening)":
        "Hello! I'm Bhavya's Personal Professional Assistant. "
        "You can ask me about her education, skills, projects, Java experience, "
        "DSA, or career interests.",

    # ---------------- ABOUT ----------------

    r"(who is bhavya|who is she|about bhavya|tell me about bhavya|introduce bhavya)":
        "Bhavya Sri is a final-year B.Tech Computer Science student specializing "
        "in Artificial Intelligence and Machine Learning. She is interested in "
        "software engineering, backend development, Java, and AI-related technologies.",


    r"(about her|tell me about her|introduce her|who are you)":
        "Bhavya is a final-year B.Tech CSE student with a focus on software "
        "development, Java, DSA, and AI/ML. "
        "She enjoys building practical projects and preparing for software engineering roles.",


    # ---------------- EDUCATION ----------------

    r"(education|educational background|degree|college|qualification|academic background)":
        "Bhavya is pursuing a B.Tech in Computer Science and Engineering "
        "with a specialization in Artificial Intelligence and Machine Learning. "
        "She is currently in her final year.",


    r"(cgpa|gpa|academic score|percentage)":
        "Bhavya's current CGPA is 8.37.",


    # ---------------- PROGRAMMING LANGUAGES ----------------

    r"(programming languages|coding languages|languages does she know|what languages)":
        "Bhavya primarily works with pythoh and also has good knowledge in Java",


    r"(java|java experience|java skills|core java)":
        "Java is one of Bhavya's primary technical skills. "
        "She has worked with Core Java, OOP concepts, collections, exception handling, "
        "and Java-based problem solving. She is also learning backend development with Spring Boot.",


    r"(python|python experience|python skills)":
        "Bhavya has experience using Python for programming, NLP-related projects, "
        "AI/ML experimentation, and building practical applications.",



    # ---------------- DSA ----------------

    r"(dsa|data structures|algorithms|data structures and algorithms)":
        "Bhavya has practiced more than 250 DSA problems, primarily using Java. "
        "Her preparation includes arrays, strings, hashing, sliding window, linked lists, "
        "trees, recursion, backtracking, sorting, searching, and other common interview topics.",


    r"(leetcode|coding problems|coding practice|problem solving)":
        "Bhavya has solved 250+ coding and DSA problems and uses these problems "
        "to strengthen her Java problem-solving and interview preparation.",


    # ---------------- SKILLS ----------------

    r"(technical skills|skills|tech skills|what are her skills)":
        "Bhavya's technical skills include Java, Python, C++, SQL, Spring Boot, "
        "MongoDB, DSA, OOP, REST APIs, Git, GitHub, IntelliJ IDEA, and VS Code.",


    r"(backend|backend development|backend skills)":
        "Bhavya is interested in backend development and has worked with Java, "
        "Spring Boot, REST APIs, databases, and backend-oriented projects.",


    r"(spring|spring boot|springboot)":
        "Bhavya has basic practical experience with Spring Boot and has used it "
        "to build a Java-based REST API project.",


    r"(sql|database|databases|mysql|h2|mongodb)":
        "Bhavya has experience with SQL and databases including MySQL and H2, "
        "and has also worked with MongoDB.",


    r"(git|github|version control)":
        "Bhavya uses Git and GitHub for source-code management and project development.",


    # ---------------- PROJECTS ----------------

    r"(projects|projects has she built|her projects|what projects)":
        "Bhavya has worked on projects including a Spring Boot API Rate Limiter, "
        "a Personal Professional FAQ Chatbot, and a StudyMate RAG project.",


    r"(api rate limiter|rate limiter|rate limiting)":
        "Bhavya developed a Spring Boot API Rate Limiter using the Token Bucket algorithm. "
        "The project includes IP-based traffic control, request logging, concurrent request handling, "
        "and HTTP 429 responses when the rate limit is exceeded.",


    r"(token bucket|token bucket algorithm)":
        "The API Rate Limiter uses the Token Bucket algorithm. "
        "Tokens are added to a bucket at a defined rate, and each API request consumes a token. "
        "When tokens are unavailable, the request is rejected.",


    r"(expense tracker|expense tracking)":
        "Bhavya has also worked on a small Expense Tracker project using HTML, CSS, and JavaScript.",


    r"(faq chatbot|personal chatbot|this chatbot|chatbot project)":
        "This Personal Professional FAQ Chatbot is a Python-based rule-driven NLP project. "
        "It uses NLTK for text preprocessing, regular expressions for FAQ pattern matching, "
        "and Streamlit for the interactive user interface.",


    r"(rag|studymate|study mate|rag project)":
        "Bhavya is also working on StudyMate, a document-based RAG application designed "
        "to retrieve relevant information from study material and generate useful answers.",


    # ---------------- AI / ML ----------------

    r"(ai|artificial intelligence|machine learning|ml|ai ml)":
        "Bhavya specializes academically in Artificial Intelligence and Machine Learning "
        "and has practical exposure to NLP, machine learning concepts, generative AI, "
        "and retrieval-augmented generation.",


    r"(generative ai|gen ai|genai|llm|large language model)":
        "Bhavya has been learning Generative AI concepts including LLMs, embeddings, "
        "RAG, prompt engineering, vector databases, and AI application development.",


    r"(nlp|natural language processing)":
        "Bhavya has practical exposure to NLP through projects involving text preprocessing, "
        "tokenization, pattern matching, and chatbot development.",


    # ---------------- CAREER ----------------

    r"(career goal|career objective|career interests|what does she want)":
        "Bhavya is targeting software engineering and backend development roles, "
        "particularly Java-based development opportunities.",


    r"(job|jobs|role|roles|looking for|looking to)":
        "Bhavya is looking for software engineering, Java development, backend development, "
        "and related technical opportunities.",


    r"(java developer|software engineer|sde|backend developer)":
        "Bhavya is interested in Java Developer, Software Engineer, SDE, and Backend Developer roles.",


    # ---------------- INTERVIEW ----------------

    r"(interview|interview preparation|technical interview)":
        "Bhavya is actively preparing for software engineering interviews with a focus on "
        "Java, DSA, OOP, SQL, backend development, projects, and AI-related concepts.",


    r"(oop|object oriented programming|object oriented)":
        "Bhavya has studied core OOP concepts including encapsulation, inheritance, "
        "polymorphism, abstraction, overloading, overriding, and static method behavior.",


    # ---------------- TOOLS ----------------

    r"(tools|development tools|ide|ides|software tools)":
        "Bhavya has worked with IntelliJ IDEA, VS Code, Git, GitHub, Maven, and related development tools.",
    # ---------------- STRENGTHS ----------------

    r"(strengths|strong points|strong skills|what is she good at)":
        "Bhavya's strengths include Java programming, DSA problem solving, OOP, "
        "backend-oriented development, and learning new technologies through hands-on projects.",

    # ---------------- CONTACT ----------------

    r"(contact|contact details|email|mail|reach her|how to contact)":
        "For professional contact information, please refer to Bhavya's resume or professional portfolio.",

    # ---------------- GOODBYE ----------------

    r"(bye|goodbye|see you|exit|quit)":
        "Thank you for visiting Bhavya's Professional Assistant. Have a great day!"
}