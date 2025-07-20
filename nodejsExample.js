import { ChatGroq } from '@langchain/groq'
import { createToolCallingAgent } from 'langchain/agents'
import { AgentExecutor } from 'langchain/agents'
import { ChatPromptTemplate } from '@langchain/core/prompts'
import { WikipediaQueryRun } from '@langchain/community/tools/wikipedia_query_run'
import getCurrentWeatherTool from './currentWeatherTool.js'
import dotenv from 'dotenv'
dotenv.config()

const model = new ChatGroq({
	apiKey: process.env.GROQ_API_KEY,
	model: 'llama-3.3-70b-versatile'
})

const wikipediaTool = new WikipediaQueryRun({
	topKResults: 1,
	maxDocContentLength: 4000
})

const myTool = new DynamicTool({
	name: 'name of tool',
	description: 'description of tool',
	func: (param:string) => {
		return 'result'
	}
})
  
const tools = [myTool, wikipediaTool] // etc...

  // your completion here
const prompt = ChatPromptTemplate.fromMessages([
  ['system', 'You are ...'],
  [
    'human',
    'I want ask you about {input}'
  ],
  ['placeholder', '{agent_scratchpad}'] // dont remove this line
])

const agent = createToolCallingAgent({ llm: model, tools: tools, prompt })
const agentExecutor = new AgentExecutor({ agent, tools })

  // your input here
const res = await agentExecutor.invoke({ input: 'AI' })
console.log(res.output)
