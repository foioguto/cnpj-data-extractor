import time
from app.src.excel_handler import ExcelHandler
from app.src.services import CNPJService
from app.src.config import config

def main():
    # --- Configuration ---
    FILE_NAME = config.file_name
    CNPJ_COLUMN = config.cnpj_column
    START_ROW = config.start_row

    print("🚀 Starting Automation Pipeline...")
    
    excel = ExcelHandler(FILE_NAME)
    service = CNPJService()
    
    records_processed = 0

    try:
        # THE PIPELINE LOOP
        # 'get_cnpjs_generator' yields one CNPJ at a time.
        for row_num, cnpj in excel.get_cnpjs_generator(CNPJ_COLUMN, START_ROW):
            
            print(f"[{records_processed + 1}] Processing Row {row_num}: {cnpj}...")
            
            # 1. Fetch Data
            company_data = service.fetch_company_data(cnpj)
            
            # 2. Update Excel (in memory)
            excel.update_row(row_num, company_data)
            
            records_processed += 1
            
            # (Optional) Sleep to respect API rate limits
            time.sleep(0.5) 

        # 3. Save everything at once (much faster than saving row by row)
        excel.save_file()
        print(f"✅ Process finished! {records_processed} records updated.")

    except Exception as e:
        print(f"❌ Fatal Error: {e}")
        # Attempts to save progress even if a crash occurs
        excel.save_file()

if __name__ == "__main__":
    main()