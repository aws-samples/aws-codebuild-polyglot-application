import { APIGatewayEvent, APIGatewayProxyResult } from 'aws-lambda';
import { DefaultDocumentClient, DocumentClientInterface, QueryInput, ScanInput, ItemList } from './lib/document_client';

const tableName = process.env.TABLE_NAME;
const client = DefaultDocumentClient;

/**
 * Returns the number of points for a customer
 * 
 * @param {number} Id
 * @param {DocumentClientInterface} client
 * @param {string} tableName
 * @returns {Promise<number>}
 */

export const findById = async (Id: String, client: DocumentClientInterface, tableName: string): Promise<string> => {
  let name: string = '';
  let params: QueryInput = {
    TableName: tableName,
    KeyConditionExpression: 'Id = :hkey',
    ExpressionAttributeValues: {
      ':hkey': Id
    }
  }

  try {
    let data = await client.query(params).promise()
    if (data.Items) {
      name = JSON.stringify(data.Items[0].Name)
    }
  } catch (error) {
    console.log(error);
    throw new Error(`Unable to query data`);
  }
  return name;
};

export const findAll = async (client: DocumentClientInterface, tableName: string): Promise<string> => {
  let names: string = '';
  let params: ScanInput = {TableName: tableName}
  
  try {
    let data = await client.scan(params).promise()
    if (data.Items) {
      names = JSON.stringify(data.Items)
    }
  } catch (error) {
    console.log(error);
    throw new Error(`Unable to scan data`);
  }
  return names;
};

/**
 * Lambda function handler that takes a HTTP event from API GW
 * 
 * @param {APIGatewayEvent} event
 * @returns {Promise<APIGatewayProxyResult>}
 */
export const handler = async (event: APIGatewayEvent): Promise<APIGatewayProxyResult> => {

  if (!tableName) {
    throw new Error('Table name is undefined');
  }

  let getVal: string;

  if (event.path === '/resources/names'){
    try {
      getVal = await findAll(client, tableName)
      console.log(getVal)
    } catch (err) {
      console.log(err);
      throw err;
    }
  }
  else if (event.pathParameters && event.pathParameters.id) {
    const Id = event.pathParameters.id;
    if (parseInt(Id) > 0 && parseInt(Id) < 8){
      try {
        getVal = await findById(Id, client, tableName)
      } catch (err) {
        console.log(err);
        throw err;
      }
    }
    else{
      return {
        statusCode: 500,
        headers: {'Access-Control-Allow-Origin': '*'},
        body: JSON.stringify({'Error': 'You entered an invalid Id'})
      };
    }
  }
  else{
    return {
      statusCode: 500,
      headers: {'Access-Control-Allow-Origin': '*'},
      body: JSON.stringify({'Error': 'Check whether you are using the right URL path'})
    };
  }

  return {
    statusCode: 200,
    headers: {'Access-Control-Allow-Origin': '*'},
    body: getVal
  };
}