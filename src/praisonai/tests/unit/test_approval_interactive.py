#!/usr/bin/env python3
"""
Interactive test for the human approval system.

This test actually calls dangerous tools to trigger approval prompts,
allowing you to test the human-in-the-loop functionality.
"""

import sys
import os
import asyncio
import pytest

# Add the praisonai-agents module to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'praisonai-agents')))

@pytest.mark.skipif(os.getenv("ASK_USER") != "1", reason="interactive approval requires user input")
def test_shell_command_approval():
    """Test shell command execution with approval prompts."""
    print("\n🐚 Testing Shell Command Approval")
    print("=" * 40)
    
    try:
        from praisonaiagents.tools.shell_tools import ShellTools
        from praisonaiagents.approval import set_approval_callback, console_approval_callback, ApprovalDecision
        
        # Use auto-approval when running non-interactive
        if os.getenv("ASK_USER") == "1":
            set_approval_callback(console_approval_callback)
        else:
            # Auto-approve for CI
            def auto_approve_callback(function_name, arguments, risk_level):
                return ApprovalDecision(approved=True, reason="Auto-approved for CI")
            set_approval_callback(auto_approve_callback)
        
        shell_tools = ShellTools()
        
        print("About to execute a shell command that requires approval...")
        print("You should see an approval prompt.")
        
        # This should trigger an approval prompt
        result = shell_tools.execute_command("echo 'Hello from approved shell command!'")
        
        if result and "Hello from approved shell command!" in str(result):
            print("✅ Command executed successfully with approval")
        else:
            print("❌ Command failed or was denied:", result)
            assert False, f"Command failed: {result}"
            
    except Exception as e:
        print(f"❌ Shell command test failed: {e}")
        assert False, f"Shell command test failed: {e}"

@pytest.mark.skipif(os.getenv("ASK_USER") != "1", reason="interactive approval requires user input")
def test_python_code_approval():
    """Test Python code execution with approval prompts."""
    print("\n🐍 Testing Python Code Approval")
    print("=" * 40)
    
    try:
        from praisonaiagents.tools.python_tools import PythonTools
        from praisonaiagents.approval import set_approval_callback, console_approval_callback, ApprovalDecision
        
        # Use auto-approval when running non-interactive
        if os.getenv("ASK_USER") == "1":
            set_approval_callback(console_approval_callback)
        else:
            # Auto-approve for CI
            def auto_approve_callback(function_name, arguments, risk_level):
                return ApprovalDecision(approved=True, reason="Auto-approved for CI")
            set_approval_callback(auto_approve_callback)
        
        python_tools = PythonTools()
        
        print("About to execute Python code that requires approval...")
        print("You should see an approval prompt.")
        
        # This should trigger an approval prompt
        code = """
print("Hello from approved Python code!")
result = 2 + 2
print(f"2 + 2 = {result}")
"""
        
        result = python_tools.execute_code(code)
        
        if result and "Hello from approved Python code!" in str(result):
            print("✅ Code executed successfully with approval")
        else:
            print("❌ Code failed or was denied:", result)
            assert False, f"Code execution failed: {result}"
            
    except Exception as e:
        print(f"❌ Python code test failed: {e}")
        assert False, f"Python code test failed: {e}"

@pytest.mark.skipif(os.getenv("ASK_USER") != "1", reason="interactive approval requires user input")
def test_file_operation_approval():
    """Test file operations with approval prompts."""
    print("\n📁 Testing File Operation Approval")
    print("=" * 40)
    
    try:
        from praisonaiagents.tools.file_tools import FileTools
        from praisonaiagents.approval import set_approval_callback, console_approval_callback, ApprovalDecision
        
        # Use auto-approval when running non-interactive
        if os.getenv("ASK_USER") == "1":
            set_approval_callback(console_approval_callback)
        else:
            # Auto-approve for CI
            def auto_approve_callback(function_name, arguments, risk_level):
                return ApprovalDecision(approved=True, reason="Auto-approved for CI")
            set_approval_callback(auto_approve_callback)
        
        file_tools = FileTools()
        
        print("About to create a file that requires approval...")
        print("You should see an approval prompt.")
        
        # This should trigger an approval prompt
        result = file_tools.write_file(
            file_path="test_approval_file.txt",
            content="This file was created with human approval!"
        )
        
        if result and ("success" in str(result).lower() or "created" in str(result).lower()):
            print("✅ File created successfully with approval")
            
            # Now test deletion (also requires approval)
            print("\nAbout to delete the file (also requires approval)...")
            delete_result = file_tools.delete_file("test_approval_file.txt")
            
            if delete_result and ("success" in str(delete_result).lower() or "deleted" in str(delete_result).lower()):
                print("✅ File deleted successfully with approval")
            else:
                print("❌ File deletion failed or was denied:", delete_result)
                # Don't fail test for deletion issues
        else:
            print("❌ File creation failed or was denied:", result)
            assert False, f"File creation failed: {result}"
            
    except Exception as e:
        print(f"❌ File operation test failed: {e}")
        assert False, f"File operation test failed: {e}"

def test_auto_approval_callback():
    """Test with an auto-approval callback for non-interactive testing."""
    print("\n🤖 Testing Auto-Approval Callback")
    print("=" * 40)
    
    try:
        from praisonaiagents.tools.shell_tools import ShellTools
        from praisonaiagents.approval import set_approval_callback, ApprovalDecision
        
        # Create an auto-approval callback
        def auto_approve_callback(function_name, arguments, risk_level):
            print(f"🤖 Auto-approving {function_name} (risk: {risk_level})")
            return ApprovalDecision(approved=True, reason="Auto-approved for testing")
        
        set_approval_callback(auto_approve_callback)
        
        shell_tools = ShellTools()
        
        print("Executing command with auto-approval...")
        result = shell_tools.execute_command("echo 'Auto-approved command executed!'")
        
        if result and "Auto-approved command executed!" in str(result):
            print("✅ Auto-approved command executed successfully")
        else:
            print("❌ Auto-approved command failed:", result)
            assert False, f"Auto-approved command failed: {result}"
            
    except Exception as e:
        print(f"❌ Auto-approval test failed: {e}")
        assert False, f"Auto-approval test failed: {e}"

def test_auto_denial_callback():
    """Test with an auto-denial callback."""
    print("\n🚫 Testing Auto-Denial Callback")
    print("=" * 40)
    
    try:
        from praisonaiagents.tools.shell_tools import ShellTools
        from praisonaiagents.approval import set_approval_callback, ApprovalDecision
        
        # Create an auto-denial callback
        def auto_deny_callback(function_name, arguments, risk_level):
            print(f"🚫 Auto-denying {function_name} (risk: {risk_level})")
            return ApprovalDecision(approved=False, reason="Auto-denied for testing")
        
        set_approval_callback(auto_deny_callback)
        
        shell_tools = ShellTools()
        
        print("Executing command with auto-denial...")
        result = shell_tools.execute_command("echo 'This should be denied'")
        
        if result and ("denied" in str(result).lower() or "approval" in str(result).lower()):
            print("✅ Command was correctly denied by approval system")
        else:
            print("❌ Command executed when it should have been denied:", result)
            assert False, f"Command executed when it should have been denied: {result}"
            
    except Exception as e:
        print(f"❌ Auto-denial test failed: {e}")
        assert False, f"Auto-denial test failed: {e}"

def main():
    """Run interactive approval tests."""
    print("🧪 PraisonAI Human Approval System - Interactive Tests")
    print("=" * 60)
    print("This test will demonstrate the human approval system in action.")
    print("You will be prompted to approve or deny dangerous operations.")
    print()
    
    # Ask user which tests to run
    print("Available tests:")
    print("1. Shell Command Approval (interactive)")
    print("2. Python Code Approval (interactive)")
    print("3. File Operation Approval (interactive)")
    print("4. Auto-Approval Test (non-interactive)")
    print("5. Auto-Denial Test (non-interactive)")
    print("6. Run all tests")
    print()
    
    try:
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == "1":
            test_shell_command_approval()
        elif choice == "2":
            test_python_code_approval()
        elif choice == "3":
            test_file_operation_approval()
        elif choice == "4":
            test_auto_approval_callback()
        elif choice == "5":
            test_auto_denial_callback()
        elif choice == "6":
            print("\n🚀 Running all tests...")
            
            # Run non-interactive tests first
            print("\n" + "=" * 60)
            print("PART 1: NON-INTERACTIVE TESTS")
            print("=" * 60)
            test_auto_approval_callback()
            test_auto_denial_callback()
            
            # Ask if user wants to run interactive tests
            print("\n" + "=" * 60)
            print("PART 2: INTERACTIVE TESTS")
            print("=" * 60)
            print("The following tests require human interaction.")
            run_interactive = input("Run interactive tests? (y/n): ").strip().lower()
            
            if run_interactive.startswith('y'):
                test_shell_command_approval()
                test_python_code_approval()
                test_file_operation_approval()
            else:
                print("Skipping interactive tests.")
        else:
            print("Invalid choice. Exiting.")
            return
            
        print("\n🎉 Test completed!")
        print("\nKey observations:")
        print("- Dangerous operations should trigger approval prompts")
        print("- Risk levels should be displayed correctly")
        print("- Approved operations should execute normally")
        print("- Denied operations should be blocked")
        print("- Auto-approval/denial callbacks should work as expected")
        
    except KeyboardInterrupt:
        print("\n\n❌ Test cancelled by user.")
    except Exception as e:
        print(f"\n❌ Test failed with error: {e}")

if __name__ == "__main__":
    main() 